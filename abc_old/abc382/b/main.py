N, D = [int(x) for x in input().split()]
# リストにして受け取るのが楽
A = list(input())
i = N - 1
while D > 0:
    # 右から見ていって、食べてないものがあったら食べ、残り日数を減らす
    if A[i] == "@":
        A[i] = "."
        D -= 1
    i -= 1

print("".join(A))
