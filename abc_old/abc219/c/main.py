X = list(input())
N = int(input())

X2 = "abcdefghijklmnopqrstuvwxyz"

order = {}
rev_order = {}
for x, y in zip(X, X2):
    order[x] = y
    rev_order[y] = x

S = [list(input()) for _ in range(N)]
S2 = ["".join([order[y] for y in x]) for x in S]

S2.sort()
print("\n".join(["".join([rev_order[y] for y in x]) for x in S2]))
