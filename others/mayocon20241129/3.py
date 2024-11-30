# https://atcoder.jp/contests/abc260/tasks/abc260_c

N, X, Y = [int(x) for x in input().split()]
jewels = [[0]*2 for _ in range(N)]
jewels[N - 1][0] += 1

for j_lv in range(N - 1, 0, -1):
    for j_col in range(2):
        same_js = jewels[j_lv][j_col]
        if j_col == 0:
            jewels[j_lv - 1][0] += same_js
            jewels[j_lv][1] += same_js * X
        else:
            jewels[j_lv - 1][0] += same_js
            jewels[j_lv - 1][1] += same_js * Y

print(jewels[0][1])
