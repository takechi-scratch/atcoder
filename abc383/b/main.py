from itertools import combinations

H, W, D = [int(x) for x in input().split()]
floor = []

for _ in range(H):
    floor.append(list(input()))

choices = []

for i in range(H):
    for j in range(W):
        if floor[i][j] == ".":
            choices.append((i, j))

max_ans = 0

for humidifier in combinations(choices, 2):
    x1, y1 = humidifier[0]
    x2, y2 = humidifier[1]
    temp_ans = 0
    for i in range(H):
        for j in range(W):
            if floor[i][j] != ".":
                continue

            if min(abs(i - x2) + abs(j - y2), abs(i - x1) + abs(j - y1)) <= D:
                temp_ans += 1

    max_ans = max(temp_ans, max_ans)

print(max_ans)
