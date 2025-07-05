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

# -------------------------------------------------------------

import itertools

N, M = [int(x) for x in input().split()]
sides = [set() for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].add(b)
    sides[b].add(a)

ans = 10 ** 18
for groups in divide_group(N):
    if not all(len(x) >= 3 for x in groups):
        continue

    now_divide_ans = 0
    need_sides = [set() for _ in range(N)]
    for group in groups:
        now_group_ans = 10 ** 18
        for perm in itertools.permutations(group):
            for i in range(-1, len(group) - 1):
                need_sides[perm[i]].add(perm[i + 1])
                need_sides[perm[i + 1]].add(perm[i])

            now_ans = 0
            for i in group:
                now_ans += len(sides[i] ^ need_sides[i])

            now_group_ans = min(now_group_ans, now_ans)

        now_divide_ans += now_group_ans

    ans = min(ans, now_divide_ans // 2)

print(ans)
