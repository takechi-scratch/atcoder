# 最大ケースで6s程度。悲しい

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

# -------------------

N = int(input())
A = [int(x) for x in input().split()]

ans = set()
for groups in divide_group_nocopy(N):
    stones = 0
    for group in groups:
        stones ^= sum(A[i] for i in group)
    ans.add(stones)

print(len(ans))
