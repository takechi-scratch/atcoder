D = input()
# 隣のペアが対になるようにリストに入れておく
hougaku = ["N", "S", "E", "W", "NE", "SW", "NW", "SE"]

# 入力された方角が偶数番目なら1個右のもの、奇数番目なら1個左のもの
if hougaku.index(D) % 2 == 0:
    print(hougaku[hougaku.index(D) + 1])
else:
    print(hougaku[hougaku.index(D) - 1])
