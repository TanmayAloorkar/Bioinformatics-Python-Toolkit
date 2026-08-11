"""Minimal parser for core VCF columns."""


def parse_vcf(vcf_file):
    """Return chromosome, position, reference, and alternate alleles from a VCF."""
    vcf_data = []
    with open(vcf_file, 'r') as input_file:
        for line in input_file:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom = fields[0]
            pos = int(fields[1])
            ref = fields[3]
            alt = fields[4]
            vcf_data.append((chrom, pos, ref, alt))
    return vcf_data
