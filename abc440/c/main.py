def solve(N: int, W: int, C: list[int]):
    ans_sum = [0] * (2 * W)
    for i, x in enumerate(C):
        ans_sum[i % (2 * W)] += x

    now_ans = sum(ans_sum[:W])
    ans = now_ans
    for start in range(2 * W):
        now_ans -= ans_sum[start]
        now_ans += ans_sum[(start + W) % (2 * W)]
        ans = min(ans, now_ans)

    return ans


T = int(input())

for _ in range(T):
    N, W = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    print(solve(N, W, C))
