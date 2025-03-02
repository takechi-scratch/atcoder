N = int(input())
# 空白区切りで整数を受け取る（これは覚えておいた方がいい）
A = [int(x) for x in input().split()]

# 1つ次のものと比較しているので、rangeの終了値はN - 1。
# index out of rangeになってしまう
for i in range(N - 1):
    if A[i] >= A[i + 1]:
        print("No")
        # Noの時点でプログラムを終了
        exit()

print("Yes")
