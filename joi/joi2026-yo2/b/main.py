N = int(input())
A = [int(x) for x in input().split()]

ans = 0
next_pass = 0
for i, x in enumerate(A):
    ans += (x + next_pass) // 3
    if (x + next_pass) // 3 > 0:
        next_pass = (x + next_pass) % 3
    else:
        next_pass = x

print(ans)
