"""Filtering helpers for FASTA records."""


def filter_fasta(input_file, output_file, header_pattern=None, sequence_content=None):
    """Copy records matching an optional header pattern and sequence fragment."""
    import re

    with open(input_file, 'r') as source, open(output_file, 'w') as destination:
        write_sequence = False
        for line in source:
            if line.startswith('>'):
                header = line.strip()
                write_sequence = True
                if header_pattern and not re.search(header_pattern, header):
                    write_sequence = False
            else:
                if write_sequence:
                    sequence = line.strip()
                    if sequence_content and sequence_content not in sequence:
                        write_sequence = False

            if write_sequence:
                destination.write(line)

    print(f"Filtered FASTA file saved to '{output_file}'.")
