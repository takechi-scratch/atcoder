N = int(input())
A = [int(x) for x in input().split()]

for i in range(N):
    # Aのうち、7i～7i+6までの部分を取り出して合計
    print(sum(A[7 * i:7 * (i + 1)]), end=" ")

# 最後に余計な空白が入るけど問題なし
print("")
