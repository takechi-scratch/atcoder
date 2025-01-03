N, M = [int(x) for x in input().split()]
num_min, num_max = -1, N
for i in range(M):
    l, r = [int(x) - 1 for x in input().split()]
    num_min = max(num_min, l)
    num_max = min(num_max, r)

print(max(num_max - num_min + 1, 0))
