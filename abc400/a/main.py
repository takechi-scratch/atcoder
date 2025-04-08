A = int(input())

ans = 400 / A

if ans % 1 == 0:
    print(int(ans))
else:
    print(-1)
