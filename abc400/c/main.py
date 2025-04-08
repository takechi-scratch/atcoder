from math import log2, sqrt, isqrt

N = int(input())

def solve(N):
    ans = 0
    for a in range(1, int(log2(N)) + 1):
        b_2_max = int(isqrt(N // (2 ** a)))
        ans += (b_2_max + 1) // 2

    return int(ans)

print(solve(N))
