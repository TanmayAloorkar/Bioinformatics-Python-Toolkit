"""Hamming distance for equal-length sequences."""


def hamming_distance(seq1, seq2):
    """Count mismatched positions in two equal-length sequences."""
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")

    return sum(a != b for a, b in zip(seq1, seq2))
