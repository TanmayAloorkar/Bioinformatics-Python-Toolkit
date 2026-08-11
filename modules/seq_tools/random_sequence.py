"""Random DNA sequence generation."""

from random import choice


def generate_random_dna(length):
    """Generate a DNA sequence of the requested length."""
    return ''.join(choice('ATGC') for _ in range(length))
