N, K = [int(x) for x in input().split()]
now = 0
i = 0
while now < K:
    now += N
    N += 1
    i += 1
print(i - 1)
