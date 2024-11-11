# 茶diff後半を落とさず解けてるのはいい感じ！！

from collections import deque
from bisect import bisect_right

Q = int(input())
d = deque([])
# 時間を変数で管理すればリストの各項目に足したりしなくていい。
time = 0
gots = 0

for i in range(Q):
    query = input()

    if query == "1":
        d.append(time)
        continue

    query_n, N = [int(x) for x in query.split()]

    if query_n == 2:
        time += N
    else:
        # 二分探索しなくてもよかったらしい。でも念のためしておくのが吉。
        gettables = bisect_right(d, time - N)
        print(gettables - gots)
        # popleftはせずに、今のところ何個収穫したのかを記録しておく。
        gots += gettables - gots

