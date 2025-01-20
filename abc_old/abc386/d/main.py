# 実装速くさせたい！！

from bisect import bisect_right

N, M = [int(x) for x in input().split()]
blacks = []
whites = []

for i in range(M):
    x, y, c = input().split()
    x, y = int(x) - 1, int(y) - 1

    if c == "B":
        blacks.append((x, y))
    else:
        whites.append((x, y))

blacks.sort(reverse=True)
whites.sort()
whites_ymin = []
temp = N
# whiteを上から見ていったとき、横yの最小値を累積
for x, y in whites:
    temp = min(temp, y)
    whites_ymin.append(temp)

whites_xkeys = [i[0] for i in whites]
for x, y in blacks:
    # どこより上がwhiteか、その時のwhiteがxよりも左だったらアウト
    index = bisect_right(whites_xkeys, x) - 1
    if index >= 0 and whites_ymin[index] <= y:
        print("No")
        break

else:
    print("Yes")
