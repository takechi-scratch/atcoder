n, m, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) - 1 for x in input().split()]

count = 0
sm = 0
for i in b:
    if a[i] < k:
        count += 1
        sm += a[i]

print(count, sm)
