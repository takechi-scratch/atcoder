X = int(input())

ans = 0
# range(開始値, 終了値-1) 1~9を2回ループ
for i in range(1, 10):
    for j in range(1, 10):
        if i * j != X:
            ans += i * j

print(ans)
