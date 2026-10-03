N, M = [int(x) for x in input().split()]
A = [0] * N
cur = 0
while M > 0:
    A[cur] += 1
    M -= 1
    cur = (cur + 1) % N

print(*A, sep="\n")
