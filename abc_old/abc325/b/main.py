N = int(input())
W = []
X = []
for _ in range(N):
    w, x = [int(i) for i in input().split()]
    W.append(w)
    X.append(x)

ans = -1

for start_time in range(24):
    oks = 0
    for i in range(N):
        # WAポイント！24時間またぎに注意。24時間ずらしてもOKってことにした。
        if X[i] + 9 <= start_time <= X[i] + 17 or X[i] + 9 <= start_time + 24 <= X[i] + 17:
            oks += W[i]

    ans = max(ans, oks)

print(ans)
