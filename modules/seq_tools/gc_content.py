"""GC-content calculations for nucleotide sequences."""


def gc_content_percent(sequence):
    """Return the percentage of G and C bases in a sequence."""
    if len(sequence) == 0:
        return 0

    total = 0
    for base in sequence:
        if base in ['G', 'C', 'g', 'c']:
            total += 1
    return (total/len(sequence)) * 100

def gc_content_sliding_window(sequence, window_size, step_size):
    """Calculate GC percentages over a sliding window."""
    if len(sequence) < window_size:
        raise ValueError("Window size is greater than sequence length")

    subseq = []
    for i in range(0, len(sequence) - window_size + 1, step_size):
        subseq.append(sequence[i:i + window_size])
    return [gc_content_percent(window) for window in subseq]

def gc_content_mult_seq(sequences_list):
    """Return the mean GC percentage across several sequences."""
    gc_content = 0
    for seq in sequences_list:
        gc_content += gc_content_percent(seq)
    avg_gc_content = gc_content / len(sequences_list)
    return avg_gc_content
