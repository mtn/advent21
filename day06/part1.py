with open("input.txt") as f:
    fish = list(map(int, f.read().strip().split(",")))

for _ in range(80):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))
