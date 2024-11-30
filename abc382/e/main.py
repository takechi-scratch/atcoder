N, X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

def check(border):
    sum_exception = 0
    for i in range(N):
        sum_exception += (P[i] / 100) * border

    return sum_exception > X


ng, ok = 0, X * 200 // N

while ok - ng > 10 ** -6:
    border = (ok + ng) / 2
    if check(border):
        ok = border
    else:
        ng = border

print((ok + ng) / 2)
