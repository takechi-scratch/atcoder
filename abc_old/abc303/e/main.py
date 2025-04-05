import sys
sys.setrecursionlimit(10 ** 7)
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

ans = []
now = -1
before = -1
for i in range(N):
    if len(sides[i]) == 1:
        now = i
        break

def tansaku(now, before):
    assert len(sides[now]) <= 2

    if len(sides[now]) == 1 or sides[now][0] != before:
        center = sides[now][0]
    else:
        center = sides[now][1]

    ans.append(len(sides[center]))

    for next_node in sides[center]:
        if next_node == now:
            continue
        if len(sides[next_node]) == 2:
            if sides[next_node][0] != center:
                tansaku(sides[next_node][0], next_node)
            else:
                tansaku(sides[next_node][1], next_node)


tansaku(now, before)
ans.sort()

print(*ans)
