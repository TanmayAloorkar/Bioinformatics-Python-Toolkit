"""Small dependency-free FASTA reader."""


def read_fasta(file_path):
    """Return FASTA records as an identifier-to-sequence dictionary."""
    sequences = {}
    with open(file_path, 'r') as fasta_file:
        identifier = None
        sequence_lines = []
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if identifier is not None:
                    sequences[identifier] = ''.join(sequence_lines)
                identifier = line[1:]
                sequence_lines = []
            else:
                sequence_lines.append(line)
        if identifier is not None:
            sequences[identifier] = ''.join(sequence_lines)
    return sequences

