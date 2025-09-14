N = int(input())
L = [int(x) for x in input().split()]
left, right = 0, N

for i in range(N):
    if L[i] == 0:
        left += 1
    else:
        break

for i in range(N - 1, -1, -1):
    if L[i] == 0:
        right -= 1
    else:
        break

print(max(0, right - left - 1))
