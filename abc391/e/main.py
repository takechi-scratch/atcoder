N = int(input())
A = [int(x) for x in list(input())]
gyakuten_changes = [1 for _ in range(3 ** N)]

for i in range(N):
    next_A = []
    next_gc = []

    for j in range(len(A) // 3):
        piece = A[j * 3 : (j + 1) * 3]
        gc_piece = gyakuten_changes[j * 3 : (j + 1) * 3]
        if piece.count(0) > piece.count(1):
            next_A.append(0)
        else:
            next_A.append(1)

        if abs(piece.count(0) - piece.count(1)) == 3:
            next_gc.append(sum(gc_piece) - max(gc_piece))

        elif piece.count(1) == 1:
            del gc_piece[piece.index(1)]
            next_gc.append(min(gc_piece))

        elif piece.count(0) == 1:
            del gc_piece[piece.index(0)]
            next_gc.append(min(gc_piece))

        else:
            raise RuntimeError

    A = next_A
    gyakuten_changes = next_gc

print(gyakuten_changes[0])
