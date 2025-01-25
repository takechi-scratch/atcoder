A = [int(x) for x in input().split()]

for i in range(4):
    a_temp = A.copy()
    temp = a_temp[i]
    a_temp[i] = a_temp[i + 1]
    a_temp[i + 1] = temp

    for j in range(4):
        if a_temp[j] > a_temp[j + 1]:
            break

    else:
        print("Yes")
        break

else:
    print("No")
