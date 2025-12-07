from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]


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


def judge(test: int) -> bool:
    # if test == 9:
    #     breakpoint()
    matched = [False] * N
    for i in range(N):
        if matched[i]:
            continue
        next_i = bisect_left(A, A[i] + test)
        while next_i < N and matched[next_i]:
            next_i += 1

        if next_i >= N:
            return False

        matched[next_i] = True
        dist = A[next_i] - A[i]
        assert dist >= test

        while True:
            now = A[next_i]
            next_i = bisect_left(A, now + dist)
            if next_i >= N or matched[next_i]:
                break

            matched[next_i] = True

    return True


if all(A[i] == i + 1 for i in range(N)):
    print(N // 2)

elif N <= 7:
    ans = -1
    for groups in divide_group_nocopy(N):
        ok = True
        min_dist = 10**18
        for group in groups:
            group = list(sorted(group))
            if len(group) == 1:
                ok = False
                break
            dist = A[group[1]] - A[group[0]]
            for i in range(1, len(group) - 1):
                if A[group[i + 1]] - A[group[i]] != dist:
                    ok = False
                    break

            if not ok:
                break
            min_dist = min(min_dist, dist)

        if ok and min_dist < 10**18:
            ans = max(min_dist, ans)

    print(ans)


else:
    # WA解法。さすがに貪欲じゃだめだね。
    ok, ng = 0, 2 * 10**9
    while ng - ok > 1:
        test = (ng + ok) // 2
        if judge(test):
            ok = test
        else:
            ng = test

    print(ok)
