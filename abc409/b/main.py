N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for x in A:
    ok_count = len([i for i in A if i >= x])
    ans = max(ans, min(ok_count, x))

print(ans)
