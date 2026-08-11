"""Coverage calculations for parsed alignment records."""


def calculate_coverage(alignment_records, reference_length):
    """Return the fraction of reference positions touched by an alignment."""
    covered_positions = set()
    for record in alignment_records:
        start = record["pos"]
        end = start + len(record["seq"])
        covered_positions.update(range(start, end))

    coverage = len(covered_positions) / reference_length
    return coverage
