from sortedcontainers import SortedList

H, W, Q = [int(x) for x in input().split()]
exploded_xs = [SortedList([]) for _ in range(H)]
exploded_ys = [SortedList([]) for _ in range(W)]

def bisect_renzoku(l, min_index=None):
    if not min_index:
        min_index = 0
    start = min_index
    max_index = len(l) - 1

    while max_index - min_index > 1:
        test = (min_index + max_index) // 2
        if l[test] - l[start] <= test - start:
            min_index = test
        else:
            max_index = test

    # 挿入したときのインデックス
    return min_index + 1

def bisect_renzoku_reverse(l, max_index=None):
    if not max_index:
        max_index = len(l) - 1
    start = max_index
    min_index = 0

    while max_index - min_index > 1:
        test = (min_index + max_index) // 2
        if l[start] - l[test] <= start - test:
            max_index = test
        else:
            min_index = test

    # 挿入したときのインデックス
    return min_index

assert bisect_renzoku_reverse([1, 2, 3, 7, 8, 10], max_index=2) == 0

ans = H * W
for _ in range(Q):
    i, j = [int(x) - 1 for x in input().split()]
    if j not in exploded_xs[i]:
        exploded_xs[i].add(j)
        exploded_ys[j].add(i)
        ans -= 1
        continue

    exp_x = exploded_xs[i]
    right = bisect_renzoku(exp_x, min_index=j) - 1
    if right == -1 and exp_x[0] - 1 >= 0:
        exp_x.add(exp_x[0] - 1)
        exploded_ys[exp_x[0] - 1].add(i)
        ans -= 1

    elif right < len(exp_x) or (right == len(exp_x) and exp_x[-1] + 1 < W):
        exp_x.add(exp_x[right - 1] + 1)
        exploded_ys[exp_x[right - 1] + 1].add(i)
        ans -= 1

    left = bisect_renzoku_reverse(exp_x, max_index=j)
    if left == -1 and exp_x[0] - 1 >= 0:
        exploded_ys[exp_x[0] - 1].add(i)
        exp_x.add(exp_x[0] - 1)
        ans -= 1

    elif left < len(exp_x) or (left == len(exp_x) and exp_x[-1] + 1 < W):
        exploded_ys[exp_x[left] - 1].add(i)
        exp_x.add(exp_x[left] - 1)
        ans -= 1

print(ans)
