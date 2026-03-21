N, K = [int(x) for x in input().split()]
A = [int(x) % K for x in input().split()]
A = list(sorted(set(A)))

now_ans = A[-1] - A[0]
for i in range(len(A) - 1):
    now_ans = min(now_ans, A[i] + K - A[i + 1])

print(now_ans)
