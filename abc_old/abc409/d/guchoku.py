def solve(N: int, S: str):
    ans = S

    for start in range(N - 1):
        for goal in range(start, N):
            after_S = list(S)
            after_S.insert(goal + 1, S[start])
            after_S.pop(start)

            now_ans = "".join(after_S)
            if now_ans < ans:
                ans = now_ans

    return ans



T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))
