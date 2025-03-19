# https://atcoder.jp/contests/abc309/tasks/abc309_c

N, K = [int(x) for x in input().split()]
AB = [tuple([int(x) for x in input().split()]) for _ in range(N)]

AB.sort(key=lambda x: x[0])
now_take_sum = sum(x[1] for x in AB)

if now_take_sum <= K:
    print(1)
    exit()

for i in range(N):
    now_take_sum -= AB[i][1]

    if now_take_sum <= K:
        print(AB[i][0] + 1)
        break
