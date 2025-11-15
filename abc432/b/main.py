# 数字の各桁ごとに受け取る
A = [int(x) for x in list(input())]
if 0 not in A:
    # 0がなければA問題と同じ
    print(*sorted(A), sep="")
    exit()
else:
    count = 0
    while 0 in A:
        A.remove(0)
        count += 1

    A.sort()
    # 0の個数を数えて、1番目と2番目の間に入れる
    ans = [A[0]] + [0] * count + A[1:]
    print(*ans, sep="")
