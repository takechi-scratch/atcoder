# TLE解法。0か1かを決め打ちするとうまくいくらしい？
# あとはvisitedの更新位置も要考察。

# 解説で使われてたライブラリを使ったら通ってしまった…()

N, M = [int(x) for x in input().split()]
A = [int(x) - 1 for x in input().split()]
B = [int(x) - 1 for x in input().split()]

sides = [[] for _ in range(N)]
visited = [False] * N

for i, j in zip(A, B):
    sides[i].append(j)
    sides[j].append(i)

for start in range(N):
    if visited[start]:
        continue

    visited[start] = True
    dfs = [(start, set([start]), set(), 1)]

    while len(dfs) > 0:
        now, history_1, history_2, count = dfs.pop()

        for next_point in sides[now]:
            if next_point in history_1 and (count + 1) % 2 != 1:
                print("No")
                exit()

            if next_point in history_2 and (count + 1) % 2 != 0:
                print("No")
                exit()

            if visited[next_point]:
                continue

            if (count + 1) % 2 == 0:
                dfs.append((next_point, history_1, history_2 | {next_point}, count + 1))
            else:
                dfs.append((next_point, history_1 | {next_point}, history_2, count + 1))

            visited[next_point] = True

print("Yes")
