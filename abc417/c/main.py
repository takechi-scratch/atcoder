from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]

A_plus = Counter([x + i + 1 for i, x in enumerate(A)])
A_minus = Counter([x - (i + 1) for i, x in enumerate(A)])

ans = 0
for x in A_plus.keys():
    ans += A_plus[x] * A_minus[-x]

print(ans)
