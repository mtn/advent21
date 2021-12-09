with open("input.txt") as f:
    nums = list(map(int, f.read().strip().split(",")))

l, r = min(nums), max(nums)

def c(n):
    return n * (n+1) // 2

mincost = 1e9
for x in range(l, r+1):
    cost = 0
    for n in nums:
        cost += c(abs(n - x))
    mincost = min(mincost, cost)

print(mincost)
