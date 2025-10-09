# 法則に気づけないと時間を溶かすことがある

# 今回の場合、必ず3秒以内にゴールできる
# （色が異なる場合、同じ色ワープ→隣が異なる色へ→同じ色ワープで必ずOK）

N, Q = [int(x) for x in input().split()]
S = list(input())


def get_dist(x, y):
    m1, m2 = max(x, y), min(x, y)
    return min(m1 - m2, m2 + N - m1)


if all(x == S[0] for x in S):
    print("1\n" * Q, end="")
    exit()


nearest = [(10**18, None)] * N

decided = -1
now = 0
now_color = S[0]
while True:
    if now_color != S[now % N]:
        for i in range(decided + 1, now):
            if nearest[i % N][0] > now - i:
                nearest[i % N] = (now - i, now % N)
        decided = now - 1
        if decided >= N - 1:
            break

        now_color = S[now]

    now += 1

decided = N
now = N - 1
now_color = S[now]
while True:
    if now_color != S[now % N]:
        for i in range(decided - 1, now, -1):
            if nearest[i % N][0] > i - now:
                nearest[i % N] = (i - now, now % N)
        decided = now + 1
        if decided <= 0:
            break

        now_color = S[now]

    now -= 1


for _ in range(Q):
    x, y = [int(x) - 1 for x in input().split()]
    if S[x] == S[y]:
        print(1)
        continue

    print(int(min(get_dist(x, y), nearest[y][0] + 1, nearest[x][0] + 1, 3)))
