"""Basic descriptive statistics for nucleotide sequences."""


def sequence_stats(sequence):
    """Print and return length, composition, skew, and molecular weight."""
    length = len(sequence)
    gc_count = sequence.count('G') + sequence.count('C')
    at_count = sequence.count('A') + sequence.count('T') + sequence.count('U')
    n_count = sequence.count('N')

    gc_skew = (sequence.count('G') - sequence.count('C')) / (gc_count) if gc_count > 0 else 0

    molecular_weight = (sequence.count('A') * 313.21 +
                        sequence.count('T') * 304.2 +
                        sequence.count('U') * 290.17 +
                        sequence.count('G') * 329.21 +
                        sequence.count('C') * 289.18)

    stats = {
        'Length': length,
        'GC Count': gc_count,
        'AT Count': at_count,
        'N Count': n_count,
        'GC Skew': gc_skew,
        'Molecular Weight': molecular_weight
    }

    print("Sequence Statistics:")
    print(f"Length: {length}")
    print(f"GC Count: {gc_count}")
    print(f"AT Count: {at_count}")
    print(f"N Count: {n_count}")
    print(f"GC Skew: {gc_skew:.4f}")
    print(f"Molecular Weight: {molecular_weight:.2f} g/mol")
    return stats

