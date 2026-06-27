N = int(input())
H = [int(x) for x in input().split()]

lo, hi = 0, 10**18

while goal - start > 1:
    mid1 = start + (goal - start) // 3

    mid2 = start + (goal - start) * 2 // 3

    if dist1 < dist2:
        goal = mid2
    else:
        start = mid1
