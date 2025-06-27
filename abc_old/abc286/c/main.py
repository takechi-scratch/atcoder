N, A, B = [int(x) for x in input().split()]
S = input()

S = S + S
ans = 10 ** 18
for start in range(N):
    now_ans = start * A
    diff_count = 0
    for i, j in zip(range(N), reversed(range(N))):
        if S[i + start] != S[j + start]:
            diff_count += 1

    diff_count //= 2
    now_ans += diff_count * B
    ans = min(ans, now_ans)

print(ans)
