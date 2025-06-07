def solve(N: int, S: str):
    start = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            start = i
            break

    if start == -1:
        return S

    goal = N - 1
    for i in range(start + 1, N):
        if S[start] < S[i]:
            goal = i - 1
            break

    after_S = list(S)
    after_S.insert(goal + 1, S[start])
    after_S.pop(start)

    return "".join(after_S)



T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))
