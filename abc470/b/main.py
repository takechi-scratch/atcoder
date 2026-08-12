N = int(input())
C = [int(x) for x in input().split()]
max_count = 0
for x in C:
    max_count = max(max_count, C.count(x))

print(N - max_count)
