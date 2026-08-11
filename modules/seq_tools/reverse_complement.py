"""Reverse complements for DNA and RNA sequences."""


def reverse_complement(sequence):
    """Return a whitespace-free reverse complement while preserving case."""
    sequence = "".join(sequence.split())

    has_thymine = 'T' in sequence or 't' in sequence
    has_uracil = 'U' in sequence or 'u' in sequence
    if has_thymine and has_uracil:
        raise ValueError("Sequence cannot contain both thymine (T) and uracil (U).")

    if has_uracil:
        complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G',
                      'a': 'u', 'u': 'a', 'g': 'c', 'c': 'g'}
    else:
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
                      'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}

    complemented_sequence = ""
    for base in sequence:
        if base not in complement:
            raise ValueError(f"Invalid base '{base}' found in the sequence.")
        complemented_sequence += complement[base]

    return complemented_sequence[::-1]
