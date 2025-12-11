#!/usr/bin/env python
"""
Utility script to inspect randomness files or strings.

Usage:
    python generate-entropy-report.py --bits 010101
    python generate-entropy-report.py --file samples/bits.txt
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path


def load_bits(args: argparse.Namespace) -> str:
    if args.bits:
        return "".join(ch for ch in args.bits.strip() if ch in {"0", "1"})
    if args.file:
        path = Path(args.file)
        return "".join(ch for ch in path.read_text().strip() if ch in {"0", "1"})
    raise ValueError("Provide either --bits or --file")


def entropy(bits: str) -> float:
    if not bits:
        return 0.0
    zeros = bits.count("0")
    ones = len(bits) - zeros
    total = len(bits)
    p0 = zeros / total if zeros else 1e-9
    p1 = ones / total if ones else 1e-9
    return -p0 * math.log2(p0) - p1 * math.log2(p1)


def main():
    parser = argparse.ArgumentParser(description="Entropy report generator")
    parser.add_argument("--bits", help="Raw bitstring to evaluate")
    parser.add_argument("--file", help="Path to text file containing bits")
    args = parser.parse_args()

    bitstring = load_bits(args)
    ent = entropy(bitstring)
    bias = abs(bitstring.count("0") - bitstring.count("1")) / len(bitstring) if bitstring else 0

    print("Length:", len(bitstring))
    print("Entropy (per bit):", round(ent, 4))
    print("Estimated total entropy:", round(ent * len(bitstring), 4))
    print("Bias:", round(bias, 6))


if __name__ == "__main__":
    main()

