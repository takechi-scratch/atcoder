from itertools import permutations

N, K = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def remove_lezero(s: str):
    ss = list(reversed(s))
    while len(ss) > 0 and ss[-1] == "0":
        ss.pop()
    if len(ss) == 0:
        return "0"
    else:
        return "".join(reversed(ss))


ans = "0"
for x in permutations(range(N), K):
    now_ans = "".join([S[i] for i in x])
    ans = max(ans, remove_lezero(now_ans), key=lambda x: (len(x), tuple(x)))

print(ans)
