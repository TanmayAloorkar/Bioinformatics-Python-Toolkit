"""GC-skew calculations."""


def gc_skew(sequence):
    """Return ``(G - C) / (G + C)`` for a sequence."""
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be a string")

    if not sequence:
        raise ValueError("Sequence must not be empty")

    g_count = sequence.count('G')
    c_count = sequence.count('C')

    if g_count + c_count == 0:
        return 0

    return (g_count - c_count) / (g_count + c_count)
