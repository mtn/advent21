with open("input.txt") as f:
    depths = list(map(int, f.read().strip().split()))

inc = 0
for d1, d2 in zip(depths, depths[1:]):
    if d2 > d1:
        inc += 1

print(inc)

