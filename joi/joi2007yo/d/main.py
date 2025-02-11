N = int(input())
M = int(input())
card = list(range(1, N * 2 + 1))

for _ in range(M):
    change = int(input())

    if change > 0:
        card = card[change:] + card[:change]

    else:
        next_card = []
        for i in range(N):
            next_card.append(card[i])
            next_card.append(card[N + i])

        card = [x for x in next_card]

print(*card, sep="\n")
