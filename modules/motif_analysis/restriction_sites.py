"""Restriction-enzyme recognition site searches."""

import re


RESTRICTION_ENZYMES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "PstI": "CTGCAG",
    "XhoI": "CTCGAG",
    "SmaI": "CCCGGG",
}


def find_restriction_sites(sequence, enzymes=RESTRICTION_ENZYMES):
    """Return enzyme recognition sites and their 1-based positions."""
    sequence = re.sub(r"\s+", "", sequence).upper()

    invalid_bases = set(sequence) - set("ATCG")
    if invalid_bases:
        invalid = ", ".join(sorted(invalid_bases))
        raise ValueError(f"Invalid DNA base(s): {invalid}")

    results = {}
    for enzyme, recognition_site in enzymes.items():
        recognition_site = recognition_site.upper()
        positions = [
            match.start() + 1
            for match in re.finditer(f"(?={re.escape(recognition_site)})", sequence)
        ]

        if positions:
            results[enzyme] = {
                "recognition_site": recognition_site,
                "positions": positions,
            }

    return results
