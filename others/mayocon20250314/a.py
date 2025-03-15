x, a, b = [int(x) for x in input().split()]
if abs(x - a) < abs(x - b):
    print("A")
else:
    print("B")
