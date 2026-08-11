"""Levenshtein distance for biological sequences."""


def edit_distance(seq1, seq2):
    """Count the insertions, deletions, and substitutions between two sequences."""
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    distance_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    for i in range(len_seq1 + 1):
        distance_matrix[i][0] = i
    for j in range(len_seq2 + 1):
        distance_matrix[0][j] = j

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                cost = 0
            else:
                cost = 1

            distance_matrix[i][j] = min(
                distance_matrix[i - 1][j] + 1,
                distance_matrix[i][j - 1] + 1,
                distance_matrix[i - 1][j - 1] + cost,
            )

    return distance_matrix[len_seq1][len_seq2]
