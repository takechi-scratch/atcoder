N, Q = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
balls = [0] * N

for x in X:
    if x > 0:
        balls[x - 1] += 1
        print(x, end=" ")
        continue

    smallest, record = -1, 10 ** 9
    for i, y in enumerate(balls):
        if y < record:
            smallest = i
            record = y

    balls[smallest] += 1
    print(smallest + 1, end=" ")
