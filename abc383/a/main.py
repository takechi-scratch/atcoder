N = int(input())
T = []
V = []

for _ in range(N):
    t, v = [int(x) for x in input().split()]
    T.append(t)
    V.append(v)

time = 0
water = 0
while True:
    water = max(0, water - 1)
    if time in T:
        water += V[T.index(time)]
        if T.index(time) == N - 1:
            break

    time += 1

print(water)
