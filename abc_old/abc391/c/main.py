N, Q = [int(x) for x in input().split()]
# 箱にどのハトがいるかのリストと
box = [set([i]) for i in range(N)]
# ハトがどの箱にいるかのリストを持っておく
hato = [i for i in range(N)]
ans = 0

for _ in range(Q):
    query = [int(x) for x in input().split()]

    if query[0] == 1:
        move_hato, move_to = query[1] - 1, query[2] - 1
        move_from = hato[move_hato]

        # 箱から去るときに1羽になるなら答えを-1
        if len(box[move_from]) == 2:
            ans -= 1

        # Setの使い方は覚えておいた方が便利
        box[move_from].remove(move_hato)
        box[move_to].add(move_hato)

        hato[move_hato] = move_to

        # 箱に来るときに1羽になるなら答えを+1
        if len(box[move_to]) == 2:
            ans += 1

    elif query[0] == 2:
        print(ans)

