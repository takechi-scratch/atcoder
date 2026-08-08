from itertools import combinations

N, K = [int(x) for x in input().split()]
clothes = [[int(x) for x in input().split()] for _ in range(N)]

best_score = 0
for choice in combinations(range(N), K):
    selected_clothes = [clothes[i] for i in choice]
    selected_clothes.sort()

    ok = True
    score = 10**18
    for i in range(K - 1):
        if not selected_clothes[i][1] < selected_clothes[i + 1][0]:
            ok = False
            break
        score = min(score, selected_clothes[i + 1][0] - selected_clothes[i][1])

    if ok:
        best_score = max(best_score, score)

if best_score == 0:
    print(-1)
else:
    print(best_score)
