N = int(input())
R = [int(x) for x in input().split()]
count = [0] * max(R)
for x in R:
    count[x - 1] += 1

now = 0
for x in count:
    now = max(0, now - x)
    now += x

print(now)
