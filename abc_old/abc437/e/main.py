import sys

sys.setrecursionlimit(10**7)

N = int(input())
sides = [[] for _ in range(N + 1)]
add_as = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    x, y = [int(x) for x in input().split()]
    sides[x].append(i)
    add_as[x].append(y)


def dfs(now: list[int]):
    global ans
    ans.extend(now)

    next_info = []
    for x in now:
        next_info.extend(list(zip(add_as[x], sides[x])))

    if len(next_info) == 0:
        return

    next_info.sort()
    next_add_a = -1
    next_now = []
    for add_a, next_node in next_info:
        if next_add_a == -1:
            next_add_a = add_a

        if add_a != next_add_a:
            dfs(next_now)
            next_now = []
            next_add_a = add_a

        next_now.append(next_node)

    if len(next_now) > 0:
        dfs(next_now)


ans = []
dfs([0])
print(*ans[1:])
