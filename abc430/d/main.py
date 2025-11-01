# SortedSetを使って人を管理、追加した隣の最短だけを更新して、いい感じに

from sortedcontainers import SortedSet

N = int(input())
X = [int(x) for x in input().split()]

people = SortedSet([(0, X[0]), (2 * 10**18, -1)])
ans = X[0]
for new_x in X:
    people.add((new_x, -1))
    i = people.index((new_x, -1))
    if new_x - people[i - 1][0] >= people[i + 1][0] - new_x:
        nearest_x = people[i + 1][0]
    else:
        nearest_x = people[i - 1][0]
    ans += abs(nearest_x - new_x)
    people.pop(i)
    people.add((new_x, abs(nearest_x - new_x)))

    if people[i - 1][1] > 0:
        neighbor_x = people[i - 1][0]
        new_score = new_x - people[i - 1][0]
        if people[i - 1][1] > new_score:
            ans += new_score - people[i - 1][1]
            people.pop(i - 1)
            people.add((neighbor_x, new_score))
    if people[i + 1][1] > 0:
        neighbor_x = people[i + 1][0]
        new_score = people[i + 1][0] - new_x
        if people[i + 1][1] > new_score:
            ans += new_score - people[i + 1][1]
            people.pop(i + 1)
            people.add((neighbor_x, new_score))

    print(ans)
