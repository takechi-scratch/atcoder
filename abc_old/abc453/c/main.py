from itertools import product

N = int(input())
L = [int(x) for x in input().split()]

max_ans = 0
for moves in product(range(2), repeat=N):
    now = 0
    ans = 0
    for i, move in enumerate(moves):
        if move == 0:
            d = L[i]
        else:
            d = 0 - L[i]

        next_pos = now + d

        if (now >= 0 and next_pos < 0) or (now < 0 and next_pos >= 0):
            ans += 1

        now = next_pos

    max_ans = max(max_ans, ans)

print(max_ans)
