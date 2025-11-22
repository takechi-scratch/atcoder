X, Y, Z = [int(x) for x in input().split()]

for i in range(10**5):
    if X + i == (Y + i) * Z:
        print("Yes")
        break

else:
    print("No")
