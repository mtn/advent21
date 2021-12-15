from collections import Counter

segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

seg_counts = {s: len(v) for s,v in segments.items()}
freqs = Counter(seg_counts.values())

for n in [1,4,7,8]:
    assert freqs[seg_counts[n]] == 1

match_lens = {seg_counts[n] for n in [1,4,7,8]}

ans = 0
with open("input.txt") as f:
    for line in f:
        output_digits = line.strip().split(" | ")[1].split()
        for d in output_digits:
            ans += len(d) in match_lens

print(ans)
