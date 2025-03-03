N = int(input())
A = [int(x) for x in input().split()]
for i in range(N):
    A[i] -= i + 1

A.sort()

sum_A = [0]
for x in A:
    sum_A.append(sum_A[-1] + x)

ans = 10 ** 20
for i, b in enumerate(A):
    now_ans = 0

    # 右側
    now_ans += sum_A[-1] - sum_A[i + 1]
    now_ans -= A[i] * (N - i - 1)

    # 左側
    now_ans += A[i] * i
    now_ans -= sum_A[i]

    ans = min(ans, now_ans)

print(ans)
