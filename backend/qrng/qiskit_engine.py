from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Tuple

from django.conf import settings

from .extractor import get_extractor

try:
    from qiskit import QuantumCircuit, transpile
except ImportError:  # pragma: no cover - fallback for environments without qiskit
    QuantumCircuit = None
    transpile = None

try:
    from qiskit_aer import Aer
except ImportError:  # pragma: no cover
    Aer = None

try:
    from qiskit import IBMQ
except ImportError:  # pragma: no cover
    IBMQ = None


class QiskitNotInstalled(Exception):
    """Raised when qiskit/aer are missing."""


@dataclass
class QrngResult:
    bits: str
    hex_value: str
    entropy: float
    bias: float


class QuantumRandomGenerator:
    """Encapsulates circuit generation and post-processing."""

    def __init__(self, mode: str = "simulator", extractor_mode: str = "von_neumann"):
        self.mode = mode
        self.extractor_mode = extractor_mode

        if QuantumCircuit is None or transpile is None:
            raise QiskitNotInstalled(
                "qiskit is not installed. Install qiskit and qiskit-aer to run the QRNG."
            )

    def generate(self, bits: int) -> QrngResult:
        raw_bits = self._generate_raw_bits(bits * 2)
        extractor = get_extractor("hash" if self.extractor_mode == "hash" else "von_neumann")
        processed = extractor.extract(raw_bits)

        if not processed:
            processed = raw_bits[:bits]
        elif len(processed) < bits:
            repetitions = bits // len(processed) + 1
            processed = (processed * repetitions)[:bits]
        else:
            processed = processed[:bits]

        entropy, bias = self._estimate_entropy(processed)

        return QrngResult(
            bits=processed,
            hex_value=self._bits_to_hex(processed),
            entropy=entropy,
            bias=bias,
        )

    def _generate_raw_bits(self, shots: int) -> str:
        backend = self._get_backend()
        circuit = QuantumCircuit(1, 1)
        circuit.h(0)
        circuit.measure(0, 0)

        compiled = transpile(circuit, backend)
        job = backend.run(compiled, shots=shots, memory=True)
        result = job.result()
        memory = result.get_memory()
        return "".join(memory)

    def _get_backend(self):
        if self.mode == "ibmq":
            return self._get_ibmq_backend()
        return self._get_simulator_backend()

    def _get_simulator_backend(self):
        if Aer is None:
            raise QiskitNotInstalled(
                "qiskit-aer is required for simulator mode. Install it via pip."
            )

        try:
            return Aer.get_backend("aer_simulator")
        except Exception:  # pragma: no cover - fallback for legacy backends
            return Aer.get_backend("qasm_simulator")

    def _get_ibmq_backend(self):
        if IBMQ is None:
            raise RuntimeError("IBMQ provider is unavailable. Install qiskit-ibmq-provider.")

        token = settings.IBMQ_TOKEN
        if not token:
            raise RuntimeError("IBMQ token not configured. Set IBMQ_TOKEN env variable.")

        backend_name = os.getenv("IBMQ_BACKEND", "ibmq_qasm_simulator")

        if IBMQ.active_account():
            try:
                provider = IBMQ.get_provider(hub="ibm-q")
            except Exception:  # pragma: no cover
                provider = IBMQ.providers()[0]
        else:
            provider = IBMQ.enable_account(token)
        return provider.get_backend(backend_name)

    @staticmethod
    def _bits_to_hex(bits: str) -> str:
        if not bits:
            return ""
        width = (len(bits) + 3) // 4
        return format(int(bits, 2), f"0{width}x")

    @staticmethod
    def _estimate_entropy(bits: str) -> Tuple[float, float]:
        if not bits:
            return 0.0, 0.0
        zeros = bits.count("0")
        ones = len(bits) - zeros
        total = len(bits)
        
        # Handle edge cases where all bits are the same
        if zeros == 0 or ones == 0:
            return 0.0, 1.0  # Zero entropy, maximum bias
            
        p0 = zeros / total
        p1 = ones / total

        entropy = -p0 * math.log2(p0) - p1 * math.log2(p1)
        bias = abs(zeros - ones) / total
        return entropy, bias

