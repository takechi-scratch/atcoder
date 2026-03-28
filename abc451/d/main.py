from sortedcontainers import SortedSet

N = int(input())

candidates = [1]
while candidates[-1] < 10**9:
    candidates.append(candidates[-1] * 2)


good_nums = SortedSet()
dfs = candidates[:]
while len(dfs) > 0:
    now = dfs.pop()
    if now in good_nums:
        continue
    good_nums.add(now)

    for extend_num in candidates:
        next_num = str(now) + str(extend_num)
        if len(next_num) >= 10:
            continue

        dfs.append(int(next_num))

# print(len(good_nums))
print(good_nums[N - 1])
