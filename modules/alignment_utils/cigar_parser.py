"""CIGAR parsing helpers for SAM alignment records."""


def parse_cigar(input_file):
    """Read a SAM file and return its CIGAR operations as ``(code, length)`` pairs."""
    cigar_operations = []

    with open(input_file, "r") as sam_file:
        for line in sam_file:
            if line.startswith("@"):
                continue
            fields = line.strip().split("\t")
            cigar_string = fields[5]
            operations = []
            length = ""
            for char in cigar_string:
                if char.isdigit():
                    length += char
                else:
                    operations.append((char, int(length)))
                    length = ""
            cigar_operations.append(operations)

    return cigar_operations
