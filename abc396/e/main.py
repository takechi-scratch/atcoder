import sys
sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]
sides_xors = [{} for _ in range(N)]
xors = [[] for _ in range(N)]

for _ in range(M):
    x, y, z = [int(x) for x in input().split()]
    x -= 1
    y -= 1

    if x == y:
        if z != 0:
            print(-1)
            exit()
        continue

    if y in sides_xors[x]:
        if sides_xors[x][y] != z:
            print(-1)
            exit()
        continue

    sides_xors[x][y] = z
    sides_xors[y][x] = z

visited = [False] * N
finished = [False] * N
history = [0]

def tansaku(now: int):
    visited[now] = True
    for next_node in sides_xors[now]:
        if finished[next_node]:
            continue

        if visited[next_node]:
            test_xor = 0
            before = next_node
            for x in reversed(history):
                test_xor = test_xor ^ sides_xors[before][x]
                if x == next_node:
                    break
                before = x

            if test_xor != 0:
                print(-1)
                exit()

            continue

        history.append(next_node)
        tansaku(next_node)
        history.pop()

    finished[now] = True


tansaku(0)

# 総和の最小

temp_xor = [0] * N
dfs = [0]
dfs[0] = 0
while len(dfs) > 0:
    now = dfs.pop()
    for next_node in sides_xors[now]:
        if temp_xor[next_node] is not None:
            continue
        temp_xor[next_node] = temp_xor[now] ^ sides_xors[now][next_node]
        dfs.append(next_node)

next_xor = set()
for x in temp_xor:
    next_xor.add(bin(x)[2:])
temp_xor = next_xor

max_digits = len(max(temp_xor, key=len))  # 注意

next_xor = set()
for i, x in enumerate(temp_xor):
    next_xor.add("0" * (max_digits - len(x)) + x)
temp_xor = next_xor

digit_zero_nodes = [0] * max_digits
for i in range(max_digits):
    for j in range(N):
        sitakara = max_digits - i - 1
        if len(temp_xor[j]) <= sitakara:
            continue

        if temp_xor[j][sitakara] == "0":
            digit_zero_nodes[i] += 1

for i in range(max_digits - 1, -1, -1):
    if digit_zero_nodes[i] == N // 2:
        continue

    if digit_zero_nodes[i] > N // 2:
        for i in range(len(temp_xor)):
            if temp_xor[i][max_digits - i - 1] == "1":
                break
        else:
            continue

        while i < len(temp_xor):
            if temp_xor[i][max_digits - i - 1] == "0":
                temp_xor.discard(temp_xor[i])
            else:
                i += 1

    else:
        for i in range(len(temp_xor)):
            if temp_xor[i][max_digits - i - 1] == "0":
                break
        else:
            continue

        while i < len(temp_xor):
            if temp_xor[i][max_digits - i - 1] == "1":
                temp_xor.discard(temp_xor[i])
            else:
                i += 1

    if len(temp_xor) == 1:
        break

print(temp_xor[0])
