N, L = [int(x) for x in input().split()]
lines = []
for _ in range(L):
    lines.append([])
    column = input().split("|")
    for i, x in enumerate(column):
        if x == "-":
            lines[-1].append(i)

now = (list(input()).index("o") + 2) // 2

for i in range(L - 1, -1, -1):
    if now in lines[i]:
        now += 1
    elif now - 1 in lines[i]:
        now -= 1

print(now)
