# 実際にシミュレーション→知っている問題に置き換え（右上をとるやつ）
# 1.8s / 2.0s。TLギリギリになるのが辛い

from itertools import product

N = int(input())
people = [[int(x) for x in input().split()] for _ in range(N)]


def solve_1():
    return len(set(x[0] for x in people))


def solve_2():
    ans = N
    for are_given in product(range(2), repeat=N):
        reached = set()
        for i, x in enumerate(are_given):
            if x == 1:
                reached.add(i)

        for p in range(N):
            if are_given[p] == 0:
                continue

            for target in range(N):
                if p == target:
                    continue

                if abs(people[p][0] - people[target][0]) <= people[p][1] - people[target][1]:
                    reached.add(target)

        gave_count = len([x for x in are_given if x == 1])
        if len(reached) == N and ans > gave_count:
            ans = gave_count

    return ans


def solve_3(people: list[list[int]]):
    people = list(set(people))
    N = len(people)
    needs = set(range(N))

    for g in range(N):
        given = people[g]
        for t in range(N):
            if g == t:
                continue

            target = people[t]

            if target[1] - target[0] <= given[1] - given[0] and target[1] + target[0] <= given[1] + given[0]:
                needs.discard(t)

    return len(needs)


def solve_4(people: list[list[int]]):
    people = list(set(people))
    N = len(people)

    compare_points = [(y - x, y + x) for x, y in people]
    compare_points.sort(key=lambda x: (-x[0], -x[1]))

    max_y = -(10**18)
    ans = 0
    for x, y in compare_points:
        if y > max_y:
            ans += 1
            max_y = y

    return ans


ans = None
if all(people[0][1] == x[1] for x in people):
    now_ans = solve_1()
    assert ans is None or now_ans == ans
    ans = now_ans

if N <= 16:
    now_ans = solve_2()
    assert ans is None or now_ans == ans
    ans = now_ans

if N <= 1000:
    now_ans = solve_3([tuple(y for y in x) for x in people])
    assert ans is None or now_ans == ans
    ans = now_ans

now_ans = solve_4([tuple(y for y in x) for x in people])
assert ans is None or now_ans == ans
ans = now_ans

print(ans)
