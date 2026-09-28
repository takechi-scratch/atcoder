N = int(input())
A = [int(x) for x in input().split()]
ans = [0, 0, 0]
for x in A:
    if x % 1000 == 0:
        continue

    change = 1000 - x % 1000
    ans[0] += change % 10
    change //= 10
    ans[1] += change % 10
    change //= 10
    ans[2] += change

print(*ans)
