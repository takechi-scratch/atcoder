# https://atcoder.jp/contests/abc221/tasks/abc221_d
N = int(input())
A, B = {}, {}
A_set, B_set = set(), set()
max_day = -1
dekigoto_dates = []

# 前計算がなかなか長くなったなあ
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    b = a + b
    dekigoto_dates.append(a)
    dekigoto_dates.append(b)

    if a not in A_set:
        A_set.add(a)
        A[a] = 0
    A[a] += 1
    if b not in B_set:
        B_set.add(b)
        B[b] = 0
    B[b] += 1

# これはポイント！変化のある日のみに絞って繰り返す。
# これをしなかったのでTLEするところでした
dekigoto_dates = list(set(dekigoto_dates))
dekigoto_dates.sort()
# 今の人数を記録しておいて、ログイン開始→+1、終了→-1
login = 0
ans = [0] * N
for i, x in enumerate(dekigoto_dates):
    if x in A_set:
        login += A[x]
    if x in B_set:
        login -= B[x]

    if login != 0:
        ans[login - 1] += dekigoto_dates[i + 1] - x

# テンプレコード、配列のまとめて出力
print(*ans)
