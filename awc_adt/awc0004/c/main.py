N = int(input())
H = [int(x) for x in input().split()]
H.sort()

if H[-1] < 0:
    print(-H[0] * 2)
elif H[0] > 0:
    print(H[-1] * 2)
else:
    print((H[-1] - H[0]) * 2)
