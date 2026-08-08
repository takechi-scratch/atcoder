from time import time
import random

start_time = time()


N, K = [int(x) for x in input().split()]
S = input()
all_o_count = S.count("o")
best_ans = all_o_count / N

cache = {}


def check(start: int, end: int, o_count: int):
    if (start, end, o_count) in cache:
        return cache[(start, end, o_count)]

    if end - start == 1:
        return 0

    if S[start] == "x":
        start += 1
    elif S[end - 1] == "x":
        end -= 1
    else:
        o_count -= 1
        if random.random() < 0.5:
            start += 1
        else:
            end -= 1

    return


while time() - start_time < 1.9:
    start, end = random.randrange(N), random.randrange(N)
    if end == start:
        continue
    elif end > start:
        start, end = end, start
    end += 1
    o_count = S[start:end].count("o")

    while end - start > 1:
        if S[start] == "x":
            start += 1
        elif S[end - 1] == "x":
            end -= 1
        else:
            o_count -= 1
            if random.random() < 0.5:
                start += 1
            else:
                end -= 1

        if o_count < K:
            break

        best_ans = max(best_ans, o_count / (end - start))


print(best_ans)
