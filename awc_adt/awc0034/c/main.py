from collections import deque

N, K, T, C = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

decs = deque([0] * K)
now_default_plus = 0
ans_count = 0
for i in range(N):
    now_default_plus -= decs.popleft()
    now_count = max(0, T - A[i] - now_default_plus)
    ans_count += now_count

    now_default_plus += now_count
    decs.append(now_count)

print(ans_count * C)
