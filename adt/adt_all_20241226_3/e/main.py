# https://atcoder.jp/contests/abc254/tasks/abc254_c
N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

groups = [[] for _ in range(K)]

for i, x in enumerate(A):
    groups[i % K].append(x)

for x in groups:
    x.sort()

now = -1
for i in range(N):
    x = groups[i % K][i // K]
    if x < now:
        print("No")
        break
    now = x
else:
    print("Yes")
