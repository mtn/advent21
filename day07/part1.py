with open("input.txt") as f:
    nums = list(map(int, f.read().strip().split(",")))

l, r = min(nums), max(nums)

mincost = 1e9
for x in range(l, r+1):
    cost = 0
    for n in nums:
        cost += abs(n - x)
    mincost = min(mincost, cost)

print(mincost)
