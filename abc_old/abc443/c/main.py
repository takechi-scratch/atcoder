N, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.append(T)

ans = 0
next_on = 0
for x in A:
    if next_on < x:
        ans += min(100, T - x)
        next_on = x + 100

print(T - ans)
