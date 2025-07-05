from collections import deque

def solve(N: int, P: list[int]):
    ans = deque([[i] for i in P])

    for now_turn in range(N):
        next_ans = deque()
        for _ in range(len(ans) // 2):
            one, two = ans.popleft(), ans.popleft()
            if one[0] < two[0]:
                next_ans.append(one + two)
            else:
                next_ans.append(two + one)

        ans = next_ans

    return ans[0]


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    P = [int(x) for x in input().split()]
    ans.append(solve(N, P))

for x in ans:
    print(*x)
