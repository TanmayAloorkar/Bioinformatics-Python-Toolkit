"""Estimate the isoelectric point of a protein sequence."""

from collections import Counter


AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")
SIDE_CHAIN_PKA = {
    "C": 8.18,
    "D": 3.65,
    "E": 4.25,
    "H": 6.00,
    "K": 10.53,
    "R": 12.48,
    "Y": 10.07,
}
N_TERMINUS_PKA = 9.69
C_TERMINUS_PKA = 2.34


def _net_charge(counts, ph):
    positive = 1 / (1 + 10 ** (ph - N_TERMINUS_PKA))
    positive += counts["H"] / (1 + 10 ** (ph - SIDE_CHAIN_PKA["H"]))
    positive += counts["K"] / (1 + 10 ** (ph - SIDE_CHAIN_PKA["K"]))
    positive += counts["R"] / (1 + 10 ** (ph - SIDE_CHAIN_PKA["R"]))

    negative = 1 / (1 + 10 ** (C_TERMINUS_PKA - ph))
    for amino_acid in ("C", "D", "E", "Y"):
        negative += counts[amino_acid] / (
            1 + 10 ** (SIDE_CHAIN_PKA[amino_acid] - ph)
        )

    return positive - negative


def isoelectric_point(sequence, precision=0.001):
    """Return the approximate pH at which a protein has zero net charge."""
    if not isinstance(sequence, str):
        raise TypeError("Protein sequence must be a string")
    if not isinstance(precision, (int, float)) or isinstance(precision, bool):
        raise TypeError("Precision must be a number")
    if precision <= 0:
        raise ValueError("Precision must be greater than zero")

    sequence = "".join(sequence.split()).upper()
    if not sequence:
        raise ValueError("Protein sequence must not be empty")

    invalid = set(sequence) - AMINO_ACIDS
    if invalid:
        raise ValueError(f"Invalid amino acid(s): {', '.join(sorted(invalid))}")

    counts = Counter(sequence)
    low, high = 0.0, 14.0
    while high - low > precision:
        midpoint = (low + high) / 2
        if _net_charge(counts, midpoint) > 0:
            low = midpoint
        else:
            high = midpoint

    return (low + high) / 2
