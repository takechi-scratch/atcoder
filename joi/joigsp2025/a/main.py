N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A = list(set(A))
A.sort()

score = 0
now = 1
for i, x in enumerate(A):
    if i == 0:
        continue

    if x - A[i - 1] == 1:
        now += 1
    else:
        score = max(score, now)
        now = 1
score = max(score, now)

print("Yes" if score >= K else "No")
