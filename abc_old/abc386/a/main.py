A = [int(x) for x in input().split()]
A_set = set(A)

if len(A_set) == 2:
    print("Yes")
else:
    print("No")

