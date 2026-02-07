N = int(input())
T = [(int(x), i + 1) for i, x in enumerate(input().split())]
T.sort()
print(T[0][1], T[1][1], T[2][1])
