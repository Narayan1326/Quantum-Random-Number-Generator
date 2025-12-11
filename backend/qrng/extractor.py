from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Protocol


class Extractor(Protocol):
    """Simple protocol for entropy extractors."""

    def extract(self, bits: str) -> str: ...


def _bits_to_bytes(bits: str) -> bytes:
    """Convert a string of bits into raw bytes."""
    if not bits:
        return b""
    # Pad to full bytes without changing entropy order by adding zeros at the end.
    padding = (8 - len(bits) % 8) % 8
    padded = bits + ("0" * padding)
    byte_arr = int(padded, 2).to_bytes(len(padded) // 8, "big")
    return byte_arr


@dataclass
class VonNeumannExtractor:
    """Removes bias by interpreting bit pairs."""

    def extract(self, bits: str) -> str:
        output = []
        # Process bits in pairs
        for i in range(0, len(bits), 2):
            # Make sure we have a complete pair
            if i + 1 >= len(bits):
                break
            pair = bits[i : i + 2]
            if pair == "01":
                output.append("0")
            elif pair == "10":
                output.append("1")
            # Ignore 00 and 11 pairs.
        return "".join(output)


@dataclass
class HashExtractor:
    """Deterministic extractor using SHA-256 digest."""

    digest_bits: int = 256

    def extract(self, bits: str) -> str:
        raw = _bits_to_bytes(bits)
        digest = sha256(raw).hexdigest()
        # Convert hex digest back to bitstring.
        digest_binary = bin(int(digest, 16))[2:].zfill(256)
        return digest_binary[: self.digest_bits]


def get_extractor(mode: str) -> Extractor:
    if mode == "hash":
        return HashExtractor()
    return VonNeumannExtractor()

