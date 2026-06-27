from bisect import bisect_right

N = int(input())
A = [int(x) for x in input().split()]

sorted_A = list(sorted(A))
ans = []
for x in A:
    ans.append(N - bisect_right(sorted_A, x))

print(*ans)
