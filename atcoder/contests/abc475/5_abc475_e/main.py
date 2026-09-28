from sortedcontainers import SortedSet

N, M, K = [int(x) for x in input().split()]
T = input()
S = [input() for _ in range(N)]
# 正解ならo, 不正解ならxにする
for i in range(N):
    correct = []
    for j in range(K):
        if S[i][j] == T[j]:
            correct.append("o")
        else:
            correct.append("x")
    S[i] = "".join(correct)

SS = SortedSet([(x, i) for i, x in enumerate(S)])

Q = int(input())
for _ in range(Q):
    i, j = [int(x) - 1 for x in input().split()]
    old_s = S[i]
    new_s = old_s[:j] + ("o" if old_s[j] == "x" else "x") + old_s[j + 1 :]
    S[i] = new_s
    SS.remove((old_s, i))
    SS.add((new_s, i))

    if M < N:
        border_s = SS[M][0]
    else:
        border_s = "x" * K

    border = SS.bisect_left((border_s, -1)) - 1
    if SS.index((new_s, i)) <= border:
        print("Yes")
    else:
        print("No")
