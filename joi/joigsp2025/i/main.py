# もうちょっと綺麗にコードが書けるようになりたい
# 小課題ごとに関数を作るのが無難か...？

from collections import defaultdict
from itertools import permutations

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]


def check_ans(ans: int):
    global final_ans
    if final_ans is None or final_ans == ans:
        final_ans = ans
    else:
        print("before_answer", final_ans)
        print("now_answer   ", ans)
        raise RuntimeError


def get_score(pair):
    cake_i, tea_i = pair
    if A[cake_i] == C[tea_i]:
        return B[cake_i] + D[tea_i]
    else:
        return B[cake_i]


final_ans = None

if all(x == 0 for x in D):
    ans = sum(x for i, x in enumerate(sorted(B, reverse=True)) if i < M)
    check_ans(ans)

if N <= 6:
    ans = 0
    for arrangements in permutations(range(N), M):
        now_ans = 0
        for tea_i in range(M):
            now_ans += get_score((arrangements[tea_i], tea_i))

        ans = max(ans, now_ans)

    check_ans(ans)

cake_brands = defaultdict(list)

for tea_i, x in enumerate(A):
    cake_brands[x].append(tea_i)

for key in cake_brands.keys():
    cake_brands[key].sort(key=lambda i: B[i])

teas = [(i, C[i], D[i]) for i in range(M)]
teas.sort(key=lambda x: x[2])
left_cakes = set(range(N))
left_teas = set(range(M))

ans = 0
pairs = []
for tea_i, tea_brand, tea_deli in reversed(teas):
    if len(cake_brands[tea_brand]) > 0:
        cake_i = cake_brands[tea_brand].pop()
        pairs.append((cake_i, tea_i))
        ans += B[cake_i] + tea_deli
        left_cakes.remove(cake_i)
        left_teas.remove(tea_i)
    else:
        pass

left_cakes = list(sorted(left_cakes, key=lambda i: B[i]))
for tea_i in range(M):
    if tea_i in left_teas:
        cake_i = left_cakes.pop()
        pairs.append((cake_i, tea_i))
        ans += B[cake_i]

pairs.sort(key=get_score)

for pair in pairs:
    if len(left_cakes) > 0 and get_score(pair) < B[left_cakes[-1]]:
        ans += B[left_cakes[-1]] - get_score(pair)
        left_cakes.pop()

check_ans(ans)

print(final_ans)
