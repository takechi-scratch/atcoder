A, B, C = [int(x) for x in input().split()]

# A == B == C のときもあるので注意
if A + B == C or B + C == A or C + A == B or A == B == C:
    print("Yes")
else:
    print("No")
