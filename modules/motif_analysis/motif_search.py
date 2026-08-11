"""Regular-expression motif searches."""


def search_motifs(sequence, motifs):
    """Return all matches for each motif pattern."""
    import re

    results = {}
    for motif in motifs:
        pattern = re.compile(motif)
        matches = pattern.findall(sequence)
        results[motif] = matches
    return results
