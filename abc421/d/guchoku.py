ti, tj, ai, aj = [int(x) for x in input().split()]
N, M, L = [int(x) for x in input().split()]

tak_moves = []
for _ in range(M):
    s, a = input().split()
    tak_moves.extend([s]*int(a))

ao_moves = []
for _ in range(L):
    s, a = input().split()
    ao_moves.extend([s]*int(a))

ans = 0
i = 0
for td, ad in zip(tak_moves, ao_moves):
    x = 1

    if td == "U":
        ti -= x
    elif td == "D":
        ti += x
    elif td == "L":
        tj -= x
    elif td == "R":
        tj += x

    if ad == "U":
        ai -= x
    elif ad == "D":
        ai += x
    elif ad == "L":
        aj -= x
    elif ad == "R":
        aj += x

    if ti == ai and tj == aj:
        ans += 1
        print(i)
        print(ti, tj, ai, aj)
    i += 1

print(ans)
