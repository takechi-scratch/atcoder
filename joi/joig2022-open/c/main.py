import sys

input = sys.stdin.readline

N = int(input())
agree_sum = [0]
for i in range(N):
    x, y = [int(x) for x in input().split()]
    agree = agree_sum[-1] - agree_sum[i - x] >= y

    agree_sum.append(agree_sum[-1] + int(agree))

print(agree_sum[-1])
