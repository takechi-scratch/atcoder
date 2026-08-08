from sortedcontainers import SortedList

H, W, N = [int(x) for x in input().split()]
pieces = [[int(x) for x in input().split()] for _ in range(N)]

sp_i = SortedList([(x[0], i) for i, x in enumerate(pieces)])
sp_j = SortedList([(x[1], i) for i, x in enumerate(pieces)])

ni, nj, used = -1, 0, 0
rev = False
appeared_i = set()
appeared_j = set()
for i in range(N):
    if pieces[i][0] in appeared_i:
        rev = False
        ni = pieces[i][0]
        break
    if pieces[i][1] in appeared_j:
        rev = True
        ni = pieces[i][1]
        break
    appeared_i.add(pieces[i][0])
    appeared_j.add(pieces[i][1])

if rev:
    H, W = W, H
    sp_i, sp_j = sp_j, sp_i
    pieces = [[x[1], x[0]] for x in pieces]


ans = [None] * N
k = 0
while k < len(sp_i):
    i, index = sp_i[k]
    if i != ni:
        k += 1
        continue

    used += 1
    ans[index] = [0, nj]

    nj += pieces[index][1]
    sp_i.remove((ni, index))
    sp_j.remove((pieces[index][1], index))

increase_j = False
while used <= N:
    if increase_j:
        # iが同じものを足してjにつなぐ
        now_index = sp_i.bisect_left((ni, -1))
        while now_index < len(sp_i) and sp_i[now_index][0] == ni:
            _, k = sp_i.pop(now_index)
            sp_j.remove((pieces[k][1], k))
            ans[k] = [0, nj]
            nj += pieces[k][1]
            used += 1
    else:
        now_index = sp_j.bisect_left((nj, -1))
        while now_index < len(sp_j) and sp_j[now_index][1] == nj:
            _, k = sp_j.pop(now_index)
            sp_i.remove((pieces[k][0], k))
            ans[k] = [ni, 0]
            ni += pieces[k][0]
            used += 1

# 最後に1足す、revは逆に
for x, y in ans:
    if rev:
        print(y + 1, x + 1)
    else:
        print(x + 1, y + 1)
