"""Estimate the molecular weight of a protein sequence."""


AMINO_ACID_MASSES = {
    "A": 89.09, "C": 121.15, "D": 133.10, "E": 147.13,
    "F": 165.19, "G": 75.07, "H": 155.16, "I": 131.17,
    "K": 146.19, "L": 131.17, "M": 149.21, "N": 132.12,
    "P": 115.13, "Q": 146.15, "R": 174.20, "S": 105.09,
    "T": 119.12, "V": 117.15, "W": 204.23, "Y": 181.19,
}
WATER_MASS = 18.015


def protein_weight(sequence):
    """Return the approximate average molecular weight in daltons (Da)."""
    if not isinstance(sequence, str):
        raise TypeError("Protein sequence must be a string")

    sequence = "".join(sequence.split()).upper()
    if not sequence:
        raise ValueError("Protein sequence must not be empty")

    invalid = set(sequence) - set(AMINO_ACID_MASSES)
    if invalid:
        raise ValueError(f"Invalid amino acid(s): {', '.join(sorted(invalid))}")

    # Free amino-acid masses include water; each peptide bond removes one water.
    return sum(AMINO_ACID_MASSES[amino_acid] for amino_acid in sequence) - (
        (len(sequence) - 1) * WATER_MASS
    )
