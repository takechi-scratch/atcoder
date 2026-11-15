N = int(input())
A = [int(x) for x in input().split()]

appeared_nums = [0] * (N + 1)

ans = 1
for i, x in enumerate(A):
    if i > 0 and x == A[i - 1]:
        appeared_nums[x] += 1
    else:
        ans += i - appeared_nums[x]
        appeared_nums[x] += 1

print(ans)
