def solve(N: int, M: int, K: int, S: list[str], sides: list[list[int]]):
    for turn in range(2 * K, 0, -1):
        before_S = []
        for now in range(N):
            next_res = [S[next_node] for next_node in sides[now]]

            person = "A" if turn % 2 == 1 else "B"
            if person == "A":
                if all(x == "B" for x in next_res):
                    before_S.append("B")
                else:
                    before_S.append("A")
            else:
                if all(x == "A" for x in next_res):
                    before_S.append("A")
                else:
                    before_S.append("B")

        S = before_S

    return "Alice" if S[0] == "A" else "Bob"


T = int(input())
for _ in range(T):
    N, M, K = [int(x) for x in input().split()]
    S = list(input())
    sides = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(x) - 1 for x in input().split()]
        sides[u].append(v)

    print(solve(N, M, K, S, sides))
