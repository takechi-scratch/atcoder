# 全てシミュレーションする。（二重ループで、同じ値ならcontinueに注意）

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

ans = 0
for x in range(N):
    for y in range(N):
        if x == y:
            continue

        for q in range(M):
            if S[x][q] != "o" and S[y][q] != "o":
                break

        else:
            ans += 1

# (x, y) と (y, x) が別で数えられているので2で割る
print(ans // 2)
