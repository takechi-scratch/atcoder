N = int(input())
A = [int(x) for x in input().split()]

for i in range(1, N - 1):
    # WAポイント！小数での計算には注意！！（3TLE経験済み）
    # 整数で計算できるならそれがベスト。↓は比の外側と内側をかける
    if A[i] * A[1] != A[i + 1] * A[0]:
        print("No")
        break

else:
    print("Yes")
