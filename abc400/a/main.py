A = int(input())

ans = 400 / A

# floatで計算するのは悪手かも
if ans % 1 == 0:
    print(int(ans))
else:
    print(-1)
