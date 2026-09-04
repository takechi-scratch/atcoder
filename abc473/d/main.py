N, K = [int(x) for x in input().split()]
search_cache = {}


def search(now_i: int, now_K: int) -> list[list[int]]:
    if now_i * 1000 + now_K in search_cache:
        return search_cache[now_i * 1000 + now_K]

    if now_i == 1:
        if now_K < 0:
            return []
        else:
            return [[now_K]]

    ans = []
    for i_multi in range(now_K // now_i + 1):
        if now_K - i_multi * now_i < 0:
            continue
        res = search(now_i - 1, now_K - i_multi * now_i)
        for x in res:
            ans.append([i_multi] + x)

    search_cache[now_i * 1000 + now_K] = ans
    return ans


ans = search(N, K)
ans = [list(reversed(x)) for x in ans]
for x in sorted(ans):
    print(" ".join(str(y) for y in x))
