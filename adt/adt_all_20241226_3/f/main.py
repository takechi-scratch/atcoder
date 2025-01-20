# https://atcoder.jp/contests/abc360/tasks/abc360_c
N = int(input())
A = [int(x) - 1 for x in input().split()]
W = [int(x) for x in input().split()]

baggages = [[] for _ in range(N)]

for i in range(N):
    baggages[A[i]].append(W[i])

ans = 0
for x in baggages:
    if len(x) < 2:
        continue

    ans += sum(x) - max(x)

print(ans)
