"""FASTQ-to-FASTA conversion."""

import sys

def fastq_to_fasta(fastq_file, fasta_file):
    """Convert every record in a FASTQ file to FASTA format."""
    from Bio import SeqIO

    with open(fastq_file, "r") as fq, open(fasta_file, "w") as fa:
        for record in SeqIO.parse(fq, "fastq"):
            SeqIO.write(record, fa, "fasta")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fastq_to_fasta.py <input_fastq> <output_fasta>")
        sys.exit(1)

    input_fastq = sys.argv[1]
    output_fasta = sys.argv[2]

    fastq_to_fasta(input_fastq, output_fasta)
    print(f"Converted {input_fastq} to {output_fasta}")
