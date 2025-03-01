# 高橋くんが勝つ場合の数を、勝つカードの組み合わせごとにそれぞれ求める。

from collections import defaultdict

def nP2(n):
    return n * (n - 1)

K = int(input())
Tak_cards = defaultdict(int)
for x in input():
    Tak_cards[x] += 1
Aoki_cards = defaultdict(int)
for x in input():
    Aoki_cards[x] += 1

all_patterns = nP2(9 * K - 8)
Tak_win_patterns = 0

for t5 in range(1, 10):
    t_score = 0
    for i in range(1, 10):
        t_score += i * 10 ** (Tak_cards[str(i)] + (t5 == i))

    for a5 in range(1, 10):
        a_score = 0
        for i in range(1, 10):
            a_score += i * 10 ** (Aoki_cards[str(i)] + (a5 == i))

        if t_score <= a_score:
            continue

        # パターン数を求める
        # 高橋くんのカードの選び方（=枚数）*青木くんのカードの選び方。
        # 高橋くんと青木くんのカードが同じなら、青木くんは高橋くんと同じカードは選べないので-1
        Tak_win_patterns += (K - Tak_cards[str(t5)] - Aoki_cards[str(t5)]) * (K - Tak_cards[str(a5)] - Aoki_cards[str(a5)] - (t5 == a5))

print(Tak_win_patterns / all_patterns)
