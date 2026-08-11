"""Merge FASTA files while handling duplicate identifiers."""

from .read_fasta import read_fasta


def merge_fasta_files(input_files, output_file):
    """Merge FASTA files, keeping the last sequence for duplicate identifiers."""
    merged_sequences = {}

    for file_path in input_files:
        sequences = read_fasta(file_path)
        for identifier, sequence in sequences.items():
            if identifier in merged_sequences:
                print(
                    f"Warning: Duplicate identifier '{identifier}' found; "
                    "overwriting the previous sequence."
                )
            merged_sequences[identifier] = sequence

    with open(output_file, 'w') as fasta_file:
        for identifier, sequence in merged_sequences.items():
            fasta_file.write(f">{identifier}\n")
            fasta_file.write(f"{sequence}\n")

    print(
        f"Merged {len(input_files)} FASTA files into '{output_file}' "
        f"with {len(merged_sequences)} unique sequences."
    )
