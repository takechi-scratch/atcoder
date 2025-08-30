ti, tj, ai, aj = [int(x) for x in input().split()]
N, M, L = [int(x) for x in input().split()]

change_turns = []

now_turn = 0
tak_raw_moves = []
for _ in range(M):
    s, a = input().split()
    now_turn += int(a)
    tak_raw_moves.append((s, now_turn))
    change_turns.append(now_turn)

now_turn = 0
ao_raw_moves = []
for _ in range(L):
    s, a = input().split()
    now_turn += int(a)
    ao_raw_moves.append((s, now_turn))
    change_turns.append(now_turn)

# 回数を揃えたい
tak_i, ao_i = 0, 0
before_turn = 0
moves = []
for x in sorted(set(change_turns)):
    if before_turn >= tak_raw_moves[tak_i][1]:
        tak_i += 1
    if before_turn >= ao_raw_moves[ao_i][1]:
        ao_i += 1

    moves.append((tak_raw_moves[tak_i][0], ao_raw_moves[ao_i][0], x - before_turn))
    before_turn = x

# print(moves)

ans = 0
for td, ad, x in moves:
    if td == ad and ti == ai and tj == aj:
        ans += x

    elif td == "U":
        if ad == "D" and tj == aj and 2 * x >= ti - ai > 0 and (ti - ai) % 2 == 0:
            ans += 1
        elif ad == "L" and 0 < ti - ai <= x and 0 < aj - tj <= x and ti - ai == aj - tj:
            ans += 1
        elif ad == "R" and 0 < ti - ai <= x and 0 < tj - aj <= x and ti - ai == tj - aj:
            ans += 1

    elif td == "D":
        if ad == "U" and tj == aj and 2 * x >= ai - ti > 0 and (ti - ai) % 2 == 0:
            ans += 1
        elif ad == "L" and 0 < ai - ti <= x and 0 < aj - tj <= x and ai - ti == aj - tj:
            ans += 1
        elif ad == "R" and 0 < ai - ti <= x and 0 < tj - aj <= x and ai - ti == tj - aj:
            ans += 1

    elif td == "L":
        if ad == "R" and ti == ai and 2 * x >= tj - aj > 0 and (tj - aj) % 2 == 0:
            ans += 1
        elif ad == "U" and 0 < ai - ti <= x and 0 < tj - aj <= x and ai - ti == tj - aj:
            ans += 1
        elif ad == "D" and 0 < ti - ai <= x and 0 < tj - aj <= x and ti - ai == tj - aj:
            ans += 1

    elif td == "R":
        if ad == "L" and ti == ai and 2 * x >= aj - tj > 0 and (tj - aj) % 2 == 0:
            ans += 1
        elif ad == "U" and 0 < ai - ti <= x and 0 < aj - tj <= x and ai - ti == aj - tj:
            ans += 1
        elif ad == "D" and 0 < ti - ai <= x and 0 < aj - tj <= x and ti - ai == aj - tj:
            ans += 1

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

print(ans)
