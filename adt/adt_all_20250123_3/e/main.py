# https://atcoder.jp/contests/abc227/tasks/abc227_c
# 最大ケースだと、自分のPCで約6秒。意味が分かりません

N = int(input())

ans = 0

A = 1
while A ** 3 <= N:
    B = A
    while A * (B ** 2) <= N:
        max_c = int(N / (A * B))
        ans += max_c - B + 1
        B += 1

    A += 1

print(ans)
