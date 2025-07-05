N, S = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
T.insert(0, 0)

for i in range(N):
    if T[i + 1] - T[i] > S:
        print("No")
        break

else:
    print("Yes")
