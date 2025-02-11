from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
colors = defaultdict(int)

colors[A[0]] += 1
colors[A[1]] += 1
colors[B[1]] += 1

ok = True
for i in range(2, N):
    colors[A[i]] += 1
    if A[i] <= A[i - 1]:
        A[i] = A[i - 1]
        ok = False

for i in range(2, N):
    colors[B[i]] += 1
    if B[i] <= B[i - 1]:
        B[i] = B[i - 1]
        ok = False

if ok:
    if A[-1] == B[-1]:
        print(A[-1], N * 2 - 3 + colors[A[-1]])
    else:
        ac = max(A[-1], B[-1])
        print(ac, N - 1 + colors[ac])
    exit()

assert N <= 500

for i in range(1, N):
    for j in range(1, N):
        colors[max(A[i], B[j])] += 1

ans = (-1, -1)
for x in colors.keys():
    if colors[x] > ans[1] or (colors[x] == ans[1] and x > ans[0]):
        ans = (x, colors[x])

print(*ans)
