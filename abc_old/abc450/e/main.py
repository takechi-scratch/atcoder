from collections import Counter
from functools import lru_cache

X = input()
Y = input()
Q = int(input())

text_len = [len(X), len(Y)]
x_count = [1, 0]
y_count = [0, 1]

while text_len[-1] < 10**18:
    text_len.append(text_len[-1] + text_len[-2])
    x_count.append(x_count[-1] + x_count[-2])
    y_count.append(y_count[-1] + y_count[-2])


x_text_counter = Counter(X)
y_text_counter = Counter(Y)


@lru_cache(maxsize=None)
def solve(r: int, target: str):
    # [0, r) におけるxの個数
    ans = 0
    for i in range(len(text_len) - 1, 1, -1):
        if text_len[i] > r:
            continue

        ans += x_text_counter[target] * x_count[i] + y_text_counter[target] * y_count[i]
        r -= text_len[i]
        if r == 0:
            break

    return ans + (Y + X)[:r].count(target)


for _ in range(Q):
    query = input().split()
    l, r, c = int(query[0]) - 1, int(query[1]), query[2]
    print(solve(r, c) - solve(l, c))
