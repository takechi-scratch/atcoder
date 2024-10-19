# N = int(input())
N, Q = [int(x) for x in input().split()]
sizi = []

for _ in range(Q):
    sizi.append(input().split())
    sizi[-1][1] = int(sizi[-1][1])

left, right = 1, 2
ans = 0

for i in range(Q):
    if sizi[i][0] == "L":
        if left == sizi[i][1]:
            continue

        kyori = 0
        t = left
        while True:
            kyori += 1
            t = t - 1 if t > 1 else N
            if t == right:
                kyori = N * 2
                break

            if t == sizi[i][1]:
                break

        kyori_1 = kyori
        kyori = 0
        t = left

        while True:
            kyori += 1
            t = t + 1 if t < N else 1
            if t == right:
                kyori = N * 2
                break

            if t == sizi[i][1]:
                break

        ans += min(kyori_1, kyori)
        left = sizi[i][1]

    else:
        if right == sizi[i][1]:
            continue

        kyori = 0
        t = right
        while True:
            kyori += 1
            t = t - 1 if t > 1 else N
            if t == left:
                kyori = N * 2
                break

            if t == sizi[i][1]:
                break

        kyori_1 = kyori
        kyori = 0
        t = right

        while True:
            kyori += 1
            t = t + 1 if t < N else 1
            if t == left:
                kyori = N * 2
                break

            if t == sizi[i][1]:
                break

        ans += min(kyori_1, kyori)
        right = sizi[i][1]

print(ans)
