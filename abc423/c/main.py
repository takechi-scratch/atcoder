N, R = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

if all(x == 1 for x in L):
    print(0)
    exit()

left, right = 0, N

for i in range(N):
    if L[i] == 1:
        left += 1
    else:
        break

for i in range(N - 1, -1, -1):
    if L[i] == 1:
        right -= 1
    else:
        break

ans = max(0, right - left)
ans += max(0, left - R) * 2
ans += max(0, R - right) * 2
for i in range(left, right):
    if L[i] == 1:
        ans += 1

print(ans)
