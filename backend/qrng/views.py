from __future__ import annotations

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.throttling import ScopedRateThrottle

from .qiskit_engine import QuantumRandomGenerator, QiskitNotInstalled


class QuantumRandomAPIView(APIView):
    throttle_scope = "qrng"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        bits_param = request.query_params.get("bits", "256")
        mode = request.query_params.get("mode", "simulator").lower()
        extractor_mode = request.query_params.get("extractor", "von_neumann").lower()

        try:
            num_bits = int(bits_param)
        except ValueError:
            return Response({"detail": "bits must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        if num_bits <= 0 or num_bits > 4096:
            return Response(
                {"detail": "bits must be between 1 and 4096."}, status=status.HTTP_400_BAD_REQUEST
            )

        if mode not in {"simulator", "ibmq"}:
            return Response({"detail": "mode must be simulator or ibmq."}, status=status.HTTP_400_BAD_REQUEST)

        if extractor_mode not in {"von_neumann", "hash"}:
            return Response(
                {"detail": "extractor must be von_neumann or hash."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            generator = QuantumRandomGenerator(mode=mode, extractor_mode=extractor_mode)
            result = generator.generate(num_bits)
        except QiskitNotInstalled as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as exc:  # pragma: no cover - runtime errors if backend unavailable
            return Response({"detail": str(exc)}, status=status.HTTP_502_BAD_GATEWAY)

        zeros = result.bits.count("0")
        ones = len(result.bits) - zeros
        statistics = {
            "zeros": zeros,
            "ones": ones,
            "bias": result.bias,
            "entropy_per_bit": result.entropy,
        }

        payload = {
            "bits": result.bits,
            "hex": result.hex_value,
            "entropy_estimate": result.entropy * len(result.bits),
            "length": len(result.bits),
            "statistics": statistics,
        }
        return Response(payload, status=status.HTTP_200_OK)


@api_view(["GET"])
def health_check(_request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

