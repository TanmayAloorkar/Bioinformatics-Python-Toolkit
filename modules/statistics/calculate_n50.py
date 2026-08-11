def calculate_n50(lengths):
    """Calculate N50 value from sequence lengths."""
    if not lengths:
        return 0
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    cumulative = 0
    for length in sorted_lengths:
        cumulative += length
        if cumulative >= total_length / 2:
            return length
    return 0