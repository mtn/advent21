from collections import defaultdict

counts = defaultdict(int)

with open("input.txt") as f:
    for line in f:
        l, r = line.strip().split(" -> ")
        x1, y1 = map(int, l.split(","))
        x2, y2 = map(int, r.split(","))

        if x1 != x2 and y1 != y2:
            continue

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                counts[(x, y1)] += 1

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                counts[(x1, y)] += 1

tot = 0
for x, y in counts:
    if counts[(x, y)] > 1:
        tot += 1
print(tot)
