N, M = [int(x) for x in input().split()]
S = [int(x) for x in list(input())]
T = [int(x) for x in list(input())]

ans = 10**18
for start in range(N - M + 1):
    now_ans = 0
    for i in range(M):
        now_ans += (S[i + start] - T[i]) % 10
    ans = min(ans, now_ans)

print(ans)
