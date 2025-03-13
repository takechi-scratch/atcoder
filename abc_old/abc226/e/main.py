import sys
sys.setrecursionlimit(10 ** 7)
# 再帰するときは、提出前にこれを付ける！！
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

visited = [False] * N
finished = [False] * N

def tansaku(now: int, before: int):
    global used_loop

    visited[now] = True

    for next_node in sides[now]:
        if next_node == before:
            continue

        if finished[next_node]:
            continue

        if visited[next_node]:
            # 閉路調査
            if used_loop:
                print(0)
                exit()
            used_loop = True
            continue

        tansaku(next_node, now)

    finished[now] = True


ans = 1
for start in range(N):
    if finished[start]:
        continue

    used_loop = False
    tansaku(start, -1)

    if not used_loop:
        print(0)
        exit()

    ans = ans * 2 % 998244353

print(ans)
