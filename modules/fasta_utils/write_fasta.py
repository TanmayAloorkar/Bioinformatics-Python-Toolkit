"""Write individual FASTA records."""


def write_fasta(sequence, header, filename):
    """Write one sequence and header to a FASTA file."""
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{header}\n")
        fasta_file.write(f"{sequence}\n")

    print(
        f"FASTA file '{filename}' written with header '{header}' "
        f"and a sequence of length {len(sequence)}."
    )

