A = [int(x) for x in input().split()]
three, two = False, False

for i in range(1, 14):
    count = A.count(i)
    if A.count(i) >= 3 and not three:
        three = True
    elif A.count(i) >= 2 and not two:
        two = True

print("Yes" if three and two else "No")
