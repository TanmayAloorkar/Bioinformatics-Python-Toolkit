"""Calculate amino-acid composition of protein sequences."""

from collections import Counter


AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def amino_acid_composition(sequence, percentage=True):
    """Return counts or percentages for the 20 standard amino acids."""
    if not isinstance(sequence, str):
        raise TypeError("Protein sequence must be a string")

    sequence = "".join(sequence.split()).upper()
    if not sequence:
        raise ValueError("Protein sequence must not be empty")

    invalid = set(sequence) - set(AMINO_ACIDS)
    if invalid:
        raise ValueError(f"Invalid amino acid(s): {', '.join(sorted(invalid))}")

    counts = Counter(sequence)
    if not percentage:
        return {amino_acid: counts[amino_acid] for amino_acid in AMINO_ACIDS}

    length = len(sequence)
    return {
        amino_acid: (counts[amino_acid] / length) * 100
        for amino_acid in AMINO_ACIDS
    }
