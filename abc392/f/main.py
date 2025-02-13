# 解説AC。
# 「逆順」を考えるのは思いついていた→位置をリストに取っておいて、
# そこから逆算するとそれぞれの位置が分かるようになる！！

from sortedcontainers import SortedSet

N = int(input())
P = [int(x) - 1 for x in input().split()]
ans = [-1] * N

last_pos = SortedSet(range(N))

for i in range(N - 1, -1, -1):
    pos = last_pos.pop(P[i])
    ans[pos] = i + 1

print(*ans)

# びっくりするほどシンプルな解答になった
