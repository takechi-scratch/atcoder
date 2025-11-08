from bisect import bisect_right

N, L = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]


def solve_1():
    ans = []
    melon_count = L // A[0]
    for all_melons in range(N, 0, -1):
        box_count = all_melons // melon_count
        left_melons = all_melons - box_count * melon_count
        if all_melons % melon_count != 0:
            box_count += 1
        else:
            left_melons += melon_count

        ans.append((box_count, left_melons * A[0]))

    return ans


def solve_2():
    ans = []
    for start in range(N):
        now_box = 0
        box_count = 0
        for x in A[start:]:
            if now_box + x > L:
                box_count += 1
                now_box = x
            else:
                now_box += x

        ans.append((box_count + 1, now_box))

    return ans


def solve_5():
    A_sum = [0]
    for x in A:
        A_sum.append(A_sum[-1] + x)

    ans = []
    for start in range(N - 1, -1, -1):
        next_start = bisect_right(A_sum, A_sum[start] + L) - 1
        if next_start == N:
            ans.append((1, A_sum[-1] - A_sum[start]))
        else:
            next_ans = ans[start - next_start]
            ans.append((next_ans[0] + 1, next_ans[1]))

    ans.reverse()

    return ans


ans = None
if all(A[i] == A[0] for i in range(N)):
    now_ans = solve_1()
    if ans is not None and ans != now_ans:
        raise AssertionError

    ans = now_ans
    print(*[f"{x[0]} {x[1]}" for x in ans], sep="\n")
    exit()

if N <= 1000:
    now_ans = solve_2()
    if ans is not None and ans != now_ans:
        raise AssertionError

    ans = now_ans

now_ans = solve_5()
if ans is not None and ans != now_ans:
    raise AssertionError

ans = now_ans


if ans is not None:
    print(*[f"{x[0]} {x[1]}" for x in ans], sep="\n")
else:
    raise RuntimeError
