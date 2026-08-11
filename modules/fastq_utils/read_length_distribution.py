"""Read-length distributions for FASTQ data."""


def read_length_distribution(fastq_file):
    """Count reads by sequence length."""
    from Bio import SeqIO
    from collections import Counter

    lengths = []

    for record in SeqIO.parse(fastq_file, "fastq"):
        lengths.append(len(record.seq))

    length_distribution = dict(Counter(lengths))

    return length_distribution
