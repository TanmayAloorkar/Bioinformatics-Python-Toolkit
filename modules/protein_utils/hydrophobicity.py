"""Calculate protein hydrophobicity using the Kyte-Doolittle scale."""


KYTE_DOOLITTLE_SCALE = {
    "A": 1.8, "C": 2.5, "D": -3.5, "E": -3.5,
    "F": 2.8, "G": -0.4, "H": -3.2, "I": 4.5,
    "K": -3.9, "L": 3.8, "M": 1.9, "N": -3.5,
    "P": -1.6, "Q": -3.5, "R": -4.5, "S": -0.8,
    "T": -0.7, "V": 4.2, "W": -0.9, "Y": -1.3,
}


def hydrophobicity(sequence):
    """Return the mean Kyte-Doolittle hydropathy score of a protein."""
    if not isinstance(sequence, str):
        raise TypeError("Protein sequence must be a string")

    sequence = "".join(sequence.split()).upper()
    if not sequence:
        raise ValueError("Protein sequence must not be empty")

    invalid = set(sequence) - set(KYTE_DOOLITTLE_SCALE)
    if invalid:
        raise ValueError(f"Invalid amino acid(s): {', '.join(sorted(invalid))}")

    total = sum(KYTE_DOOLITTLE_SCALE[amino_acid] for amino_acid in sequence)
    return total / len(sequence)
