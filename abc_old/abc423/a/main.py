X, C = [int(x) for x in input().split()]
ans = 0
for i in range(10 ** 6):
    if i * 1000 + i * C <= X:
        ans = i * 1000
    else:
        print(ans)
        exit()
