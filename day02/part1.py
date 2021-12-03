x = y = 0

with open("input.txt") as f:
    for line in f:
        num = int(line.split()[1])
        if line.startswith("forward"):
            x += num
        elif line.startswith("down"):
            y += num
        elif line.startswith("up"):
            y -= num

print(x*y)


