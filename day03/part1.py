from collections import Counter

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

g = []
e = []
for i in range(len(lines[0])):
    c = Counter([l[i] for l in lines])
    g.append(c.most_common()[0][0])
    e.append(c.most_common()[1][0])


gamma = int("".join(g), 2)
epsilon = int("".join(e), 2)

print(gamma * epsilon)



