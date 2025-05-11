# 鳩たちを「グループ」で管理し、グループ番号と巣の位置を紐づける
# 落ち着いて考えればもっと速く解けたかな

N, Q = [int(x) for x in input().split()]
group_su = [i for i in range(N)]  # グループ番号ごとの巣の位置
su_group = [i for i in range(N)]  # 各巣ごとのグループ番号

hato_group = [i for i in range(N)]  # 各鳩ごとのグループ番号

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        # 鳩のグループ番号を更新
        a, b = query[1] - 1, query[2] - 1
        next_a_group = su_group[b]

        hato_group[a] = next_a_group

    elif query[0] == 2:
        # グループ番号で巣の位置を更新
        a, b = query[1] - 1, query[2] - 1
        su_group[a], su_group[b] = su_group[b], su_group[a]
        group_su[su_group[a]] = a
        group_su[su_group[b]] = b

    elif query[0] == 3:
        # 鳩のグループ番号から巣の位置を取得する
        a = query[1] - 1
        print(1 + group_su[hato_group[a]])
