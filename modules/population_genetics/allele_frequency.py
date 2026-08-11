"""Functions for calculating allele frequencies in a population."""


def allele_frequency(homozygous_count, heterozygous_count, population_size):
    """Calculate allele frequency from diploid genotype counts."""
    counts = (homozygous_count, heterozygous_count, population_size)
    if any(not isinstance(count, int) or isinstance(count, bool) for count in counts):
        raise TypeError("Counts and population size must be integers")
    if homozygous_count < 0 or heterozygous_count < 0:
        raise ValueError("Genotype counts cannot be negative")
    if population_size <= 0:
        raise ValueError("Population size must be greater than zero")
    if homozygous_count + heterozygous_count > population_size:
        raise ValueError("Genotype counts cannot exceed the population size")

    allele_copies = (2 * homozygous_count) + heterozygous_count
    total_alleles = 2 * population_size
    return allele_copies / total_alleles
