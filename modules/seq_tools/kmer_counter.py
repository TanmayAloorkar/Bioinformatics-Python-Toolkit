"""K-mer counts for DNA and RNA sequences."""


def count_kmers(sequence, k):
    """Count every overlapping k-mer in a sequence."""
    if k <= 0:
        raise ValueError("k must be a positive integer.")

    if len(sequence) < k:
        return {}

    kmer_counts = {}

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    return kmer_counts

