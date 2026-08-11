"""Threshold-based VCF filtering."""


def filter_vcf(
    vcf_file,
    output_file,
    qual_threshold=30,
    dp_threshold=10,
    mq_threshold=40,
    qd_threshold=2,
    fs_threshold=60,
    sor_threshold=3,
):
    """Copy VCF records that pass the configured quality thresholds."""
    with open(vcf_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('#'):
                outfile.write(line)
                continue

            fields = line.strip().split('\t')
            qual = float(fields[5]) if fields[5] != '.' else 0
            entries = (item.split('=', 1) for item in fields[7].split(';'))
            info = {parts[0]: parts[1] for parts in entries if len(parts) == 2}
            dp = int(info.get('DP', 0))
            mq = float(info.get('MQ', 0))
            qd = float(info.get('QD', 0))
            fs = float(info.get('FS', 0))
            sor = float(info.get('SOR', 0))

            passes_filters = (
                qual >= qual_threshold
                and dp >= dp_threshold
                and mq >= mq_threshold
                and qd >= qd_threshold
                and fs <= fs_threshold
                and sor <= sor_threshold
            )
            if passes_filters:
                outfile.write(line)
