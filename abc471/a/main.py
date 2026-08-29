A, B = [int(x) for x in input().split()]
print("Nine" if 9 in [A + B, A - B, A * B, A / B] else "Nein")
