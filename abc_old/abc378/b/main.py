N = int(input())
g_collects = []
for _ in range(N):
    g_collects.append([int(x) for x in input().split()])

Q = int(input())

for _ in range(Q):
    g_type, date = [int(x) for x in input().split()]
    g_collect = g_collects[g_type - 1]
    if date % g_collect[0] == g_collect[1]:
        print(date)
        continue

    # なかなか雑な数え方。回収日から何日たっているか数え、次までの日数を出す。
    print(date + g_collect[0] - ((date - g_collect[1]) % g_collect[0]))
