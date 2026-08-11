"""SNP counts from VCF files."""


def count_snps(vcf_file):
    """Count VCF rows whose reference and alternate alleles are single bases."""
    snp_count = 0

    with open(vcf_file, "r") as input_file:
        for line in input_file:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            ref_allele = fields[3]
            alt_alleles = fields[4].split(",")
            if len(ref_allele) == 1 and all(len(alt) == 1 for alt in alt_alleles):
                snp_count += 1

    return snp_count
