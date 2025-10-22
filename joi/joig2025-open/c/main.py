N, Q = [int(x) for x in input().split()]
T = list(input())
segments = [T]
for _ in range(N):
    now = segments[-1]
    next_sg = []
    for i in range(len(now) // 3):
        if now[i * 3 : (i + 1) * 3].count("A") >= 2:
            next_sg.append("A")
        else:
            next_sg.append("B")

    segments.append(next_sg)

for _ in range(Q):
    change = int(input()) - 1
    segments[0][change] = "A" if segments[0][change] == "B" else "B"
    for i in range(1, N + 1):
        change //= 3
        if segments[i - 1][change * 3 : (change + 1) * 3].count("A") >= 2:
            segments[i][change] = "A"
        else:
            segments[i][change] = "B"

    print(segments[-1][0])
