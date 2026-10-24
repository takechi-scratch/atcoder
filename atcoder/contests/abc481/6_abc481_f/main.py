from sortedcontainers import SortedSet
from collections import defaultdict

MOD = 998244353

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
scores = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = [int(x) for x in input().split()]
    sides[a - 1].append(b - 1)
    scores[a - 1].append(c)

best_score = [(10**18, 9, 0, 0)] * N
best_score[0] = (0, 0, 0, 0)

queue = SortedSet([(0, 0, 0, 0, 0)])
counter = defaultdict(int)
counter[(0, 0)] += 1

while len(queue) > 0:
    now_score_len, last_digit, _, now_score, now = queue.pop(0)
    if (now_score_len, last_digit, _) > best_score[now][:3]:
        continue

    nns = list(zip(sides[now], scores[now]))
    nns.sort(key=lambda x: x[1])

    for next_node, next_last_digit in nns:
        next_score_len = now_score_len + 1
        next_score = now_score * 10 + next_last_digit
        next_score %= MOD

        next_candicate = (next_score_len, next_last_digit)
        if next_candicate < best_score[next_node][:2]:
            best_score[next_node] = (
                next_score_len,
                next_last_digit,
                counter[(next_score_len, next_last_digit)],
                next_score,
            )
            queue.add(
                (
                    next_score_len,
                    next_last_digit,
                    counter[(next_score_len, next_last_digit)],
                    next_score,
                    next_node,
                )
            )

            counter[(next_score_len, next_last_digit)] += 1

for i in range(1, N):
    print(best_score[i][3])
