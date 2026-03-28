N = int(input())
P = [int(x) - 1 for x in input().split()]

now = 0
count = 1
while now != N - 1:
    now = P[now]
    count += 1

print(count)
