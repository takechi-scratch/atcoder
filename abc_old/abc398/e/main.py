import sys

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

color = [-1] * N
dfs = [0]
color[0] = 0
while len(dfs) > 0:
    now = dfs.pop()
    next_color = 1 - color[now]
    for next_node in sides[now]:
        if color[next_node] != -1:
            continue

        color[next_node] = next_color
        dfs.append(next_node)

nodes_0, nodes_1 = [], []
for i in range(N):
    if color[i] == 0:
        nodes_0.append(i)
    else:
        nodes_1.append(i)

choices = set()
for i in nodes_0:
    for j in nodes_1:
        if j in sides[i]:
            continue
        choices.add((i, j))

print(choices, file=sys.stderr)

if len(choices) % 2 == 0:
    print("Second")
else:
    print("First")
    me = choices.pop()
    print(min(me) + 1, max(me) + 1)

while True:
    you = [int(x) - 1 for x in input().split()]
    if you == [-2, -2]:
        break

    choices.discard((you[0], you[1]))
    choices.discard((you[1], you[0]))

    me = choices.pop()
    print(min(me) + 1, max(me) + 1)
