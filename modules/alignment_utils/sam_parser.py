"""Minimal SAM reader used by the alignment utilities."""


def parse_sam_file(sam_file):
    """Parse non-header SAM rows into dictionaries."""
    alignment_records = []

    with open(sam_file, "r") as input_file:
        for line in input_file:
            if line.startswith("@"):
                continue
            fields = line.strip().split("\t")
            record = {
                "qname": fields[0],
                "flag": int(fields[1]),
                "rname": fields[2],
                "pos": int(fields[3]),
                "mapq": int(fields[4]),
                "cigar": fields[5],
                "rnext": fields[6],
                "pnext": int(fields[7]),
                "tlen": int(fields[8]),
                "seq": fields[9],
                "qual": fields[10],
            }
            alignment_records.append(record)

    return alignment_records
