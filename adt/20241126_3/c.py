# https://atcoder.jp/contests/abc244/tasks/abc244_b

N = int(input())
S = list(input())

houkou = 0
muki_ryou = ((1, 0), (0, -1), (-1, 0), (0, 1))

x, y = 0, 0

for s in S:
    if s == "S":
        x += muki_ryou[houkou % 4][0]
        y += muki_ryou[houkou % 4][1]
    else:
        houkou += 1

print(x, y)
