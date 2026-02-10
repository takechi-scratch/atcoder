# https://atcoder.jp/contests/abc326/tasks/abc326_a
# やるだけ
X, Y = [int(x) for x in input().split()]
if 0 <= Y - X <= 2 or 0 <= X - Y <= 3:
    print("Yes")
else:
    print("No")
