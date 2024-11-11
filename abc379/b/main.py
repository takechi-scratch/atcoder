# 前から連続記録を見ていって、本数に達したら1プラス。

N, K = [int(x) for x in input().split()]
S = list(input())

cnt = 0
ans = 0
for i in range(N):
    if S[i] == "O":
        cnt += 1
    else:
        cnt = 0

    if cnt >= K:
        ans += 1
        cnt = 0


print(ans)
