N, Q = [int(x) for x in input().split()]
group_su = [i for i in range(N)]
next_gindex = N
su_group = [i for i in range(N)]

hato_group = [i for i in range(N)]

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        a, b = query[1] - 1, query[2] - 1
        next_a_group = su_group[b]

        hato_group[a] = next_a_group

    elif query[0] == 2:
        a, b = query[1] - 1, query[2] - 1
        su_group[a], su_group[b] = su_group[b], su_group[a]
        group_su[su_group[a]] = a
        group_su[su_group[b]] = b

    elif query[0] == 3:
        a = query[1] - 1
        print(1 + group_su[hato_group[a]])
