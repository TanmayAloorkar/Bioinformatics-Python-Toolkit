"""Palindrome searches for nucleotide sequences."""


def find_palindromic_sequences(sequence, min_length=4):
    """Return the start index and text of palindromes at least ``min_length`` long."""
    palindromes = []
    seq_length = len(sequence)

    for i in range(seq_length):
        for j in range(i + min_length, seq_length + 1):
            substring = sequence[i:j]
            if substring == substring[::-1]:
                palindromes.append((i, substring))

    return palindromes
