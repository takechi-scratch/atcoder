N = int(input())
Plans = [[int(x) for x in input().split()] for _ in range(N)]

t, x, y = 0, 0, 0
for plan in Plans:
    distance = abs(plan[1] - x) + abs(plan[2] - y)
    moving_time = plan[0] - t

    if distance <= moving_time and (moving_time - distance) % 2 == 0:
        t, x, y = plan
    else:
        print("No")
        break

else:
    print("Yes")
