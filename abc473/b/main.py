N = int(input())
A = [int(x) for x in input().split()]
ans = 0
for x in set(A):
    if A.count(x) % 2 == 1:
        ans += x

print(ans)
