N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for x in range(max(A) + 10):
    if len([i for i in A if i >= x]) >= x:
        ans = max(ans, x)

print(ans)
