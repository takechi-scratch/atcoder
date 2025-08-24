# 未完成（TLE解法）

from math import isqrt

X = int(input())
ans = set()

if X == 0:
    print(1)
    print(0)
    exit()

# minus = (X > 0)
# X = abs(X)

for m in range(10 ** 7):
    n_n1 = m ** 2 - X
    if n_n1 < 0:
        continue

    test_n = isqrt(n_n1)
    if test_n * (test_n + 1) == n_n1:
        ans.add(test_n)

print(len(ans))
print(*ans)
