# https://atcoder.jp/contests/abc228/tasks/abc228_a
S, T, X = [int(x) for x in input().split()]

# WAポイント！時間のやつは慣れるしかないのか…？
if S <= X < T:
    print("Yes")
# 時間が前にあるかをちゃんとチェック。
elif T < S and S <= X < T + 24:
    print("Yes")
elif X < S and S <= X + 24 < T + 24:
    print("Yes")
else:
    print("No")
