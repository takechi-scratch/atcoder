# 結局分からず。
# このコードじゃ列挙できてない！！！！

N, K = [int(x) for x in input().split()]
numbers = [[int(x) for x in input().split()] for _ in range(3)]
[x.sort() for x in numbers]

ans = sum([x[-1] for x in numbers])
index = [N - 1 for _ in range(3)]

def score(x, y, z):
    return numbers[0][x] * numbers[1][y] + numbers[2][z] * numbers[1][y] + numbers[0][x] * numbers[2][z]


for _ in range(K - 1):
    diff = []
    if index[0] > 0:
        diff.append(score(*index) - score(index[0] - 1, index[1], index[2]))
    else:
        diff.append(10 ** 10)
    if index[1] > 0:
        diff.append(score(*index) - score(index[0], index[1] - 1, index[2]))
    else:
        diff.append(10 ** 10)
    if index[2] > 0:
        diff.append(score(*index) - score(index[0], index[1], index[2] - 1))
    else:
        diff.append(10 ** 10)

    reduce_index = diff.index(min(diff))
    index[reduce_index] -= 1
    ans -= min(diff)

print(ans)
