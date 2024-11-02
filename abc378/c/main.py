# ただやるだけ。

N = int(input())
A = [int(x) for x in input().split()]

last = {}
ans = []

for i in range(N):
    if A[i] not in last:
        ans.append("-1")
    else:
        ans.append(last[A[i]])
    last[A[i]] = str(i + 1)

print(" ".join(ans))
