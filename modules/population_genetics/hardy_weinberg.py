"""Functions for calculations under Hardy-Weinberg equilibrium."""


def hardy_weinberg(allele_frequency, population_size=None):
    """Return expected Hardy-Weinberg frequencies and optional population counts."""
    if isinstance(allele_frequency, bool) or not isinstance(
        allele_frequency, (int, float)
    ):
        raise TypeError("Allele frequency must be a number")
    if not 0 <= allele_frequency <= 1:
        raise ValueError("Allele frequency must be between 0 and 1")

    if population_size is not None:
        if not isinstance(population_size, int) or isinstance(population_size, bool):
            raise TypeError("Population size must be an integer")
        if population_size <= 0:
            raise ValueError("Population size must be greater than zero")

    p = float(allele_frequency)
    q = 1.0 - p
    genotype_frequencies = {
        "AA": p**2,
        "Aa": 2 * p * q,
        "aa": q**2,
    }

    result = {
        "allele_frequencies": {"A": p, "a": q},
        "genotype_frequencies": genotype_frequencies,
    }

    if population_size is not None:
        result["expected_counts"] = {
            genotype: frequency * population_size
            for genotype, frequency in genotype_frequencies.items()
        }

    return result
