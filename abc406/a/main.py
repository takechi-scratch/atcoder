A, B, C, D = [int(x) for x in input().split()]

if A > C:
    print("Yes")
elif A == C and B >= D:
    print("Yes")
else:
    print("No")
