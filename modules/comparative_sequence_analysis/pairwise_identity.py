"""Pairwise identity for aligned sequences."""


def pairwise_identity(seq1, seq2):
    """Return the percentage of identical positions in two aligned sequences."""
    if not isinstance(seq1, str) or not isinstance(seq2, str):
        raise TypeError("Sequences must be strings")

    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")

    if not seq1:
        raise ValueError("Sequences must not be empty")

    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return (matches / len(seq1)) * 100
