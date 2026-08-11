"""Quality-based filtering for FASTQ reads."""


def quality_filter(fastq_file, min_quality=20, min_length=50):
    """Return reads meeting the minimum average quality and length thresholds."""
    from Bio import SeqIO

    filtered_sequences = []

    for record in SeqIO.parse(fastq_file, "fastq"):
        avg_quality = sum(record.letter_annotations["phred_quality"]) / len(record)
        if avg_quality >= min_quality and len(record) >= min_length:
            filtered_sequences.append(record)

    return filtered_sequences
