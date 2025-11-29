W, B = [int(x) for x in input().split()]

for x in range(10**6):
    if W * 1000 < x * B:
        print(x)
        break
