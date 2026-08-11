"""Split multi-record FASTA files."""


def split_fasta(input_file, output_dir):
    """Write each record in a FASTA file to its own file."""
    import os

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as fasta_file:
        identifier = None
        sequence_lines = []
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if identifier is not None:
                    output_file_path = os.path.join(output_dir, f"{identifier}.fasta")
                    with open(output_file_path, 'w') as output_file:
                        output_file.write(f">{identifier}\n")
                        output_file.write(''.join(sequence_lines) + '\n')
                identifier = line[1:]
                sequence_lines = []
            else:
                sequence_lines.append(line)
        if identifier is not None:
            output_file_path = os.path.join(output_dir, f"{identifier}.fasta")
            with open(output_file_path, 'w') as output_file:
                output_file.write(f">{identifier}\n")
                output_file.write(''.join(sequence_lines) + '\n')

    print(f"FASTA file '{input_file}' split into individual files in directory '{output_dir}'.")
