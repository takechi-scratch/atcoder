D, F = [int(x) for x in input().split()]
for now in range(F + 7, 10**6, 7):
    if now > D:
        print(now - D)
        break
