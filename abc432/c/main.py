from math import gcd

N, X, Y = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()

# 実験→数を調整できる最小の大きさが分かる
x_y_gcd = gcd(X, Y)
count_dist = (Y - X) // x_y_gcd
if any((A[i + 1] - A[i]) % count_dist != 0 for i in range(N - 1)):
    print(-1)
    exit()

# スタートはAiの小さい順（＝Yを多く持てる順）
x_count, y_count = 0, A[0]
ans = y_count
for i in range(N - 1):
    next_dist = A[i + 1] - A[i]
    x_count += Y // x_y_gcd * next_dist // count_dist
    y_count -= X // x_y_gcd * next_dist // count_dist

    if y_count < 0:
        print(-1)
        exit()

    ans += y_count

print(ans)
