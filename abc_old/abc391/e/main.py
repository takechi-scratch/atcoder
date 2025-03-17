# 上から下へ見ていくイメージ→形勢逆転に必要な変化数を下から記録（一種のDP）

N = int(input())
A = [int(x) for x in list(input())]
gyakuten_changes = [1 for _ in range(3 ** N)]

for i in range(N):
    next_A = []
    next_gc = []

    # それぞれの3つずつ見ていく
    for j in range(len(A) // 3):
        piece = A[j * 3 : (j + 1) * 3]
        gc_piece = gyakuten_changes[j * 3 : (j + 1) * 3]
        if piece.count(0) > piece.count(1):
            next_A.append(0)
        else:
            next_A.append(1)

        # 全て同じ色の時は、小さい順に2個（sum - max）
        if abs(piece.count(0) - piece.count(1)) == 3:
            next_gc.append(sum(gc_piece) - max(gc_piece))

        # 1が1個の時は、1にあたる変化数を消して、
        # あと2個の0の中で小さい方を変えればOK
        elif piece.count(1) == 1:
            del gc_piece[piece.index(1)]
            next_gc.append(min(gc_piece))

        # 同様
        elif piece.count(0) == 1:
            del gc_piece[piece.index(0)]
            next_gc.append(min(gc_piece))

        else:
            # これ以外はありえないので、なんか変な時のエラー
            raise RuntimeError

    A = next_A
    gyakuten_changes = next_gc

# 最後に1個だけ残る、ちなみにA[0]も最後の形勢になってるはず
print(gyakuten_changes[0])
