from collections import Counter
import re

counts = Counter()

with open("flake8_output.txt") as f:
    for line in f:
        m = re.search(r":\d+:\d+:\s+([A-Z]\d+)", line)
        if m:
            counts[m.group(1)] += 1

for code, count in counts.most_common():
    print(f"{code}: {count}")
