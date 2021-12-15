with open("input.txt") as f:
    fish = list(map(int, f.read().strip().split(",")))

memo = {}


def count(timer, days):
    global memo

    if days == 0:
        return 1

    if (timer, days) in memo:
        return memo[(timer, days)]

    if timer == 0:
        memo[(timer, days)] = count(6, days - 1) + count(8, days - 1)
    else:
        memo[(timer, days)] = count(timer - 1, days - 1)

    return memo[(timer, days)]


tot = 0
for f in fish:
    tot += count(f, 256)
print(tot)
