"""Write concise VCF variant summaries."""

from .vcf_parser import parse_vcf


def output_variant_stats(vcf_file, output_file):
    """Write total, SNP, and indel counts for a VCF file."""
    vcf_data = parse_vcf(vcf_file)
    total_variants = len(vcf_data)
    snp_count = sum(1 for _, _, ref, alt in vcf_data if len(ref) == 1 and len(alt) == 1)
    indel_count = total_variants - snp_count

    with open(output_file, 'w') as summary_file:
        summary_file.write(f"Total Variants: {total_variants}\n")
        summary_file.write(f"SNPs: {snp_count}\n")
        summary_file.write(f"Indels: {indel_count}\n")
