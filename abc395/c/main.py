from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]

left, right = -1, -1
count = defaultdict(int)
over = 0
ans = 10 ** 18

for right in range(N):
    if count[A[right]] == 1:
        over += 1
    count[A[right]] += 1

    while right > left and over > 0:
        ans = min(ans, right - left)
        if count[A[left + 1]] == 2:
            over -= 1
        count[A[left + 1]] -= 1
        left += 1

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
