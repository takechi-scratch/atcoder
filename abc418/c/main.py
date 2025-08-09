N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()

ans = [0]
for i, x in enumerate(A):
    while len(ans) < x + 1:
        ans.append(ans[-1] + N - i)

for _ in range(Q):
    b = int(input())
    if b > A[-1]:
        print(-1)
        continue

    print(ans[b - 1] + 1)
