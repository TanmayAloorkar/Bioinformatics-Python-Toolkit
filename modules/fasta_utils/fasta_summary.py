"""Summary statistics for FASTA files."""

from ..Statistics.calculate_n50 import calculate_n50

def summarize_fasta(input_file):
    """Collect sequence count, length, N50, and GC statistics from a FASTA file."""
    from Bio import SeqIO
    import numpy as np

    lengths = []
    gc_counts = []

    for record in SeqIO.parse(input_file, "fasta"):
        seq_length = len(record.seq)
        lengths.append(seq_length)
        gc_count = (record.seq.count('G') + record.seq.count('C')) / seq_length * 100
        gc_counts.append(gc_count)

    total_sequences = len(lengths)
    shortest_sequence = min(lengths) if lengths else 0
    longest_sequence = max(lengths) if lengths else 0
    average_length = np.mean(lengths) if lengths else 0
    n50 = calculate_n50(lengths)
    average_gc_content = np.mean(gc_counts) if gc_counts else 0

    summary = {
        "total_sequences": total_sequences,
        "shortest_sequence": shortest_sequence,
        "longest_sequence": longest_sequence,
        "average_length": average_length,
        "n50": n50,
        "average_gc_content": average_gc_content
    }

    return summary

