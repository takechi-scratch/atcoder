from collections import deque


def solve(N: int, D: int, A: list[int], B: list[int]):
    q = deque()
    for day, x in enumerate(zip(A, B)):
        come, use = x
        q.extend([day] * come)
        for _ in range(use):
            q.popleft()

        last = -(10**18)
        while len(q) > 0 and last <= day - D:
            last = q.popleft()

        if last > day - D:
            q.appendleft(last)

    return len(q)


T = int(input())
for _ in range(T):
    N, D = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(solve(N, D, A, B))
