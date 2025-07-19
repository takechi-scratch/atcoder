N, M = [int(x) for x in input().split()]
choices = []
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    choices.append((a, a - b))

choices.sort()

min_lose = 10 ** 18 * 2
new_choices = []
for need_bottles, lose_bottles in choices:
    if lose_bottles >= min_lose:
        continue
    new_choices.append((need_bottles, lose_bottles))
    min_lose = lose_bottles
choices = new_choices

ans = 0
for x in reversed(choices):
    # if i >= 1 and choices[i][0] == choices[i - 1][0] and choices[i][1] >= choices[i - 1][1]:
    # # Aが重複する際ははじく
    #     continue

    need_bottles, lose_bottles = x
    if N < need_bottles:
        continue

    exchangeable_times = (N - need_bottles) // lose_bottles + 1
    ans += exchangeable_times
    N -= lose_bottles * exchangeable_times

print(ans)
