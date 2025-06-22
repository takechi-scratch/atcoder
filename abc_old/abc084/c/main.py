N = int(input())
trains = [tuple(int(x) for x in input().split()) for _ in range(N - 1)]

for i in range(N):
    ans = 0
    time = 0
    for now_sta in range(i, N - 1):
        c, s, f = trains[now_sta]
        if time <= s:
            time = s
        elif time % f != 0:
            time += f - time % f

        time += c

    print(time)
