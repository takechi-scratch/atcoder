N, M = [int(x) for x in input().split()]
targets = [input() for _ in range(2)]

# いもす法の部分ごとの操作を記録
swaps = [0] * (N + 1)
for _ in range(M):
    l, r = [int(x) - 1 for x in input().split()]
    swaps[l] += 1
    swaps[r + 1] -= 1

# ansを1つずつ見ながらnowを更新し、スワップが偶数回ならS、奇数回ならT
now = 0
ans = []
for i in range(N):
    now += swaps[i]
    ans.append(targets[now % 2][i])

print("".join(ans))
