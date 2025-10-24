from functools import lru_cache
import sys

sys.setrecursionlimit(10**7)

N = int(input())


@lru_cache(maxsize=None)
def judge(x):
    if x == N:
        return True
    elif x > N:
        return False
    else:
        return judge(x + sum(int(y) for y in str(x)))


ans = 0
for x in range(1, N + 1):
    if judge(x):
        ans += 1

print(ans)
