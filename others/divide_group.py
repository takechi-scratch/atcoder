# グループ分けの場合の数はN番目の「ベル数」として知られている。

def divide_group(N: int):
    """0からN未満までの整数をグループ分けするとき、考えられる組み合わせを列挙
       N<=10くらいまでなら問題なし

    Args:
        N (int): 要素の数

    """

    assert N >= 0

    dfs = [(0, [])]
    while len(dfs) > 0:
        finished_count, groups = dfs.pop()
        if finished_count >= N:
            yield groups
            continue

        for i in range(len(groups) + 1):
            next_group = [set(y for y in x) for x in groups]
            if i == len(next_group):
                next_group.append({finished_count})
            else:
                next_group[i].add(finished_count)

            dfs.append((finished_count + 1, next_group))


def divide_group_nocopy(N: int):
    """要素ごとにコピーをしない高速化バージョン。
       N=12で0.7s, N=13で5.6s程度。

    Args:
        N (int): 要素の数

    """

    assert N >= 0

    dfs = [(0, [], -1)]
    while len(dfs) > 0:
        finished_count, groups, added_i = dfs.pop()

        if finished_count < 0:
            groups[added_i].remove(-finished_count - 1)
            if len(groups[added_i]) == 0:
                groups.pop()

            continue

        if added_i >= 0:
            if added_i == len(groups):
                groups.append({finished_count - 1})
            else:
                groups[added_i].add(finished_count - 1)

        if finished_count >= N:
            yield groups
            continue

        for i in range(len(groups) + 1):
            dfs.append((-finished_count - 1, groups, i))
            dfs.append((finished_count + 1, groups, i))



if __name__ == "__main__":
    N = 5
    for x in divide_group(N):
        print(x)

    print(f"{len(list(divide_group(N)))=}")
    print(f"{len(list(divide_group_nocopy(N)))=}")
