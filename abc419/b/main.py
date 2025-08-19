Q = int(input())
box = []
for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        box.append(query[1])
    else:
        # 最小値の場所を確認する。1回あたりO(N)だけど、時間的には問題ない。
        i = box.index(min(box))
        print(box.pop(i))
