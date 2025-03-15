from collections import deque

H, W = [int(x) for x in input().split()]
grid = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]
teleport = [set() for _ in range(26)]

normal = {".", "#", "S", "G"}
for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            start = (i, j)
            visited[i][j] = True
        elif grid[i][j] == "G":
            goal = (i, j)
        elif grid[i][j] not in normal:
            teleport[ord(grid[i][j]) - 97].add((i, j))

bfs = deque([(0, start)])

def judge(ni, nj):
    if not (0 <= ni < H and 0 <= nj < W):
        return False
    if visited[ni][nj]:
        return False
    if grid[ni][nj] == "#":
        return False

    if ni == goal[0] and nj == goal[1]:
        print(score + 1)
        exit()

    visited[ni][nj] = True
    bfs.append((score + 1, (ni, nj)))

    return True

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
while len(bfs) > 0:
    score, now = bfs.popleft()
    i, j = now
    for di, dj in moves:
        judge(i + di, j + dj)

    if grid[i][j] in normal:
        continue

    now_port = ord(grid[i][j]) - 97
    del_list = []
    for pos in teleport[now_port]:
        res = judge(*pos)
        if res:
            del_list.append(pos)

    [teleport[now_port].discard(pos) for pos in del_list]

print(-1)
