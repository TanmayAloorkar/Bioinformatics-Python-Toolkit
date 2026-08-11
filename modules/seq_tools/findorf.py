"""Open reading frame detection for DNA and RNA sequences."""

from .translate import translate

def find_orf(sequence):
    """Return translated ORFs and a short description of the longest one."""
    orfs = []

    start_codon = "AUG"
    stop_codons = {"UAA", "UAG", "UGA"}

    sequence = sequence.upper().replace("T", "U")

    for i in range(len(sequence) - 2):
        codon = sequence[i:i+3]
        if codon == start_codon:
            for j in range(i + 3, len(sequence) - 2, 3):
                next_codon = sequence[j:j+3]
                if next_codon in stop_codons:
                    orfs.append((i, j + 3))
                    break

    if orfs:
        longest_start, longest_end = max(orfs, key=lambda bounds: bounds[1] - bounds[0])
        longest_orf = translate(sequence[longest_start:longest_end])
        longest_orf_text = f"Longest ORF: {longest_orf}"
    else:
        longest_orf_text = "No ORFs found"

    translated_orfs = [
        (start, end, translate(sequence[start:end])) for start, end in orfs
    ]
    return translated_orfs, longest_orf_text
