# WA解答。累積和っぽいやり方なのかな？
# 意味を考えてからcntの足し引きをすること！！

N, M = [int(x) for x in input().split()]

segments = {x: [] for x in range(M)}

for _ in range(N):
    l, r = [int(x) - 1 for x in input().split()]
    segments[r].append(l)

ans = 0
cnt = 1
for i in range(M):
    # そこまでのコンボ数を足す
    ans += cnt

    if len(segments[i]) > 0:
        ans -= cnt - i + max(segments[i])
        cnt = i - max(segments[i]) + 1

    else:
        cnt += 1

print(ans)

# ポイント：右を固定して数えてみる
# なんとかしてO(N)に収めるしかない。→右固定では？
# それぞれの地点で数えている時点で、そこを右端とした個数と考えるべき。
# やっぱり過去問精進が物を言うのかなー