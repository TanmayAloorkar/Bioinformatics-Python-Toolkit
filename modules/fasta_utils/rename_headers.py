"""Rename headers in one FASTA file or a directory of FASTA files."""


def rename_headers(input_file, output_file, new_header):
    """Rename records in a FASTA file or every FASTA file in a directory."""
    import os

    if os.path.isdir(input_file):
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        for filename in os.listdir(input_file):
            if filename.endswith('.fasta') or filename.endswith('.fa'):
                input_path = os.path.join(input_file, filename)
                output_path = os.path.join(output_file, filename)
                rename_headers_in_file(input_path, output_path, new_header)

        print(
            f"Headers in all FASTA files in directory '{input_file}' "
            f"renamed and saved to '{output_file}'."
        )

    else:
        rename_headers_in_file(input_file, output_file, new_header)
        print(f"Headers in '{input_file}' renamed and saved to '{output_file}'.")


def rename_headers_in_file(input_path, output_path, new_header):
    """Rename records as ``new_header``, ``new_header_2``, and so on."""
    count = 0
    with open(input_path, 'r') as source, open(output_path, 'w') as destination:
        for line in source:
            if line.startswith('>'):
                count += 1
                if count == 1:
                    destination.write('>' + new_header.rstrip('\n') + '\n')
                else:
                    destination.write(
                        '>' + new_header.rstrip('\n') + '_' + str(count) + '\n'
                    )
            else:
                destination.write(line)
