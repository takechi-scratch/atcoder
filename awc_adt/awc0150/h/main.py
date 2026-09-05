N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()

left_used, right_used = 0, N - 1
c1, c2 = A[0], A[-1]
ans = c2 - c1
for _ in range(K - 1):
    assert left_used < right_used

    candidates = [
        abs(c1 - A[left_used + 1]),
        abs(c2 - A[left_used + 1]),
        abs(c1 - A[right_used - 1]),
        abs(c2 - A[right_used - 1]),
    ]
    now_ans = max(candidates)
    ans += now_ans

    if candidates[0] == now_ans:
        c1 = A[left_used + 1]
        left_used += 1
    elif candidates[1] == now_ans:
        c2 = A[left_used + 1]
        left_used += 1
    elif candidates[2] == now_ans:
        c1 = A[right_used - 1]
        right_used -= 1
    else:
        c2 = A[right_used - 1]
        right_used -= 1

print(ans)
