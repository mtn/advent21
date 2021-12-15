from collections import Counter

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

ox = set(range(len(lines)))
co = set(range(len(lines)))

for i in range(len(lines[0])):
    c = Counter([l[i] for k, l in enumerate(lines) if k in ox])
    mc = c.most_common()

    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        ox_crit = "1"
    else:
        ox_crit = mc[0][0]

    c = Counter([l[i] for k, l in enumerate(lines) if k in co])
    mc = c.most_common()

    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        co_crit = "0"
    else:
        co_crit = mc[-1][0]

    for j, l in enumerate(lines):
        if j in ox and l[i] != ox_crit:
            ox.remove(j)
        if j in co and l[i] != co_crit:
            co.remove(j)

assert len(ox) == len(co) == 1

nox = int(lines[list(ox)[0]], 2)
nco = int(lines[list(co)[0]], 2)

print(nox * nco)
