N, Q = [int(x) for x in input().split()]
X = [int(x) - 1 for x in input().split()]

S = set()
S_start = {}
score_sum = [0]
A = [0] * N

for i, change in enumerate(X):
  if change not in S:
    S.add(change)
    S_start[change] = i
  else:
    S.discard(change)
    A[change] += score_sum[-1] - score_sum[S_start[change]]
    del S_start[change]

  score_sum.append(score_sum[-1] + len(S))


for change in S:
  A[change] += score_sum[-1] - score_sum[S_start[change]]

print(*A)
