X = int(input())
now = 1

# 実際に階乗を計算しながら、一致するものがあったら終了
# rangeは引数2つで[開始, 終了)を表せる
for i in range(2, 10 ** 6):
    now *= i
    # この時点で、iの階乗がnowに格納されている
    if now == X:
        print(i)
        break
