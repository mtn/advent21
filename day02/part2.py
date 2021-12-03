x = y = 0
aim = 0

with open("input.txt") as f:
    for line in f:
        num = int(line.split()[1])
        if line.startswith("forward"):
            x += num
            y += aim * num
        elif line.startswith("down"):
            aim += num
        elif line.startswith("up"):
            aim -= num

print(x*y)


