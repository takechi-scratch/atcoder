# 本番TLE→復習でAC
# 本質としては外側から内側へ狭まっていくうちに、時計回りに回しまくる

N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))

# 2次元配列の回転の関数は使えるかも。Pythonだとコードが楽。
# WAポイント！破壊的処理に注意！list.reverse()を使うとやられます
# あと、reversed()はイテレータを返すので注意。
def kaiten(list2d, degrees=1):
    degrees = degrees % 4
    if degrees == 1:
        ans = (list(reversed(list2d)))
        # 行と列を転置する方法
        ans = [list(x) for x in zip(*ans)]
    elif degrees == 3:
        list2d = [list(x) for x in zip(*list2d)]
        ans = list(reversed(list2d))
    elif degrees == 2:
        list2d = [list(reversed(x)) for x in list2d]
        ans = list(reversed(list2d))
    else:
        return list2d

    return ans

# assert文を書くのはテストケース側でREと判定できるからアリかも
assert kaiten([[1, 2], [3, 4]], 2) == [[4, 3], [2, 1]]

# あらかじめ4回転分のリストを作っておく
lists_turning = []
for i in range(4):
    lists_turning.append(kaiten(A, i))

for i in range(N):
    for j in range(N):
        # 何段階内側へ入っているかを計算して、必要になる回転数を取り出す
        # min(min(i, N-i-1), min(j, N-j-1) （トリプルミニマム）はいらない
        print(lists_turning[(min(i, N-i-1, j, N-j-1) + 1) % 4][i][j], end="")

    print("")
