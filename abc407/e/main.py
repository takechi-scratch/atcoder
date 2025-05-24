import sys
sys.setrecursionlimit(10**7)

def solve(N: int, A: list[int], now: int = 0, decided: int = 0, left: int = 0, right: int = 0):
    if N <= decided:
        return now

    ans = now

    if decided // 2 - left < 0 and decided // 2 - right < 0 and (N - decided) * 2 > max(left, right):  # 逆さ括弧
        # print(")(")
        ans = max(ans, solve(N, A, now + A[N * 2 - decided - 1], decided + 1, left, right))

    if decided // 2 - left < 0 and (N - decided) * 2 > right:  # 右括弧
        # print("))")
        ans = max(ans, solve(N, A, now, decided + 1, left, right + 1))

    if decided // 2 - right < 0 and (N - decided) * 2 > left:  # 左括弧
        # print("((")
        ans = max(ans, solve(N, A, now + A[decided] + A[N * 2 - decided - 1], decided + 1, left + 1, right))

    if (N - decided) * 2 > max(left, right):
        # print("()")
        ans = max(ans, solve(N, A, now + A[decided], decided + 1, left + 1, right + 1))  # 正括弧

    # print("^", ans)
    return ans




T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(input()) for _ in range(N * 2)]
    print(solve(N, A))
