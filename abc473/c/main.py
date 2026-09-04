from collections import Counter

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

B = list(Counter(A).values())
max_count = max(B)
print(B.count(max_count) + B.count(max_count - 1))
