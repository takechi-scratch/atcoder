N = int(input())
A = [int(x) for x in input().split()]

affects = [[] for _ in range(N)]
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        affects[j - 1].append(i)

ans = set()
now_A = [0] * N

for i, a in reversed(list(enumerate(A))):
    if now_A[i] % 2 == a:
        continue

    ans.add(i + 1)
    for j in affects[i]:
        now_A[j - 1] += 1

print(len(ans))
print(*ans)
