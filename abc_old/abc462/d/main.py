N, D = [int(x) for x in input().split()]
candidates = [[int(x) for x in input().split()] for _ in range(N)]

possible_counts = [0] * (10**6 + 10)
for s, t in candidates:
    if t - s < D:
        continue
    possible_counts[s] += 1
    possible_counts[t - D + 1] -= 1

for i in range(1, len(possible_counts)):
    possible_counts[i] += possible_counts[i - 1]

ans = 0
for count in possible_counts:
    ans += count * (count - 1) // 2

print(ans)
