# abc391Bとほぼ同じ

N, M = [int(x) for x in input().split()]
S = []
for _ in range(N):
    S.append(list(input()))

T = []
for _ in range(M):
    T.append(list(input()))


# スタートの位置を決める
for i in range(N - M + 1):
    for j in range(N - M + 1):
        ok = True
        for di in range(M):
            for dj in range(M):
                if S[i + di][j + dj] != T[di][dj]:
                    ok = False

        if ok:
            print("Yes")
            exit()

print("No")
