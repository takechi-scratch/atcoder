from collections import defaultdict

N = int(input())
A_raw = [int(x) for x in input().split()]
B_raw = [int(x) for x in input().split()]

ans = []


counts = defaultdict(int)
counts[B_raw[0]] += 1
A = A_raw[1:]
B = B_raw[1:]

x_max = -1
for i, x in enumerate(A):
    if x < x_max:
        counts[x] += 1
        counts[x_max] -= 1
        A[i] = x_max

    x_max = max(x, x_max)

x_max = -1
for i, x in enumerate(B):
    if x < x_max:
        counts[x] += 1
        counts[x_max] -= 1
        B[i] = x_max

    x_max = max(x, x_max)

i_left = N
j_left = N

while len(A) > 0 or len(B) > 0:
    if len(A) > 0 and (len(B) <= 0 or A[-1] >= B[-1]):
        counts[A[-1]] += j_left
        i_left -= 1
        A.pop()
    else:
        counts[B[-1]] += i_left
        j_left -= 1
        B.pop()

assert i_left == j_left == 1

best_color, best_score = None, -1
for color, score in counts.items():
    if score > best_score or (score == best_score and color > best_color):
        best_color = color
        best_score = score


if N <= 500:
    boards = [[None] * N for _ in range(N)]
    boards[0] = B_raw
    for i, x in enumerate(A_raw):
        boards[i][0] = x

    for i in range(1, N):
        for j in range(1, N):
            boards[i][j] = max(boards[i - 1][j], boards[i][j - 1])

    counts_all = defaultdict(int)
    for i in range(N):
        for j in range(N):
            counts_all[boards[i][j]] += 1

    for color in counts_all.keys():
        assert counts[color] == counts_all[color]

print(int(best_color), int(best_score))
