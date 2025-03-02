N = int(input())

# 適当に-で初期化
ans = [["-"] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 各マスの模様はこの式で一発で判定できる
        # min(i, N - i - 1, j, N - j - 1)は「外側から何番目か」（0始まり）
        if min(i, N - i - 1, j, N - j - 1) % 2 == 0:
            ans[i][j] = "#"
        else:
            ans[i][j] = "."

# テンプレコード（2次元配列をまとめて出力）
# printを呼び出す回数は少ない方がいい（高速化）
print("\n".join(["".join(x) for x in ans]))

# 類題: https://qiita.com/e869120/items/43181c2084e6e5337ca9#2-4-%E9%9D%A2%E7%99%BD%E3%81%84%E5%95%8F%E9%A1%8C%E3%81%8C%E5%87%BA%E9%A1%8C%E3%81%95%E3%82%8C%E3%82%8B%E3%81%93%E3%81%A8%E3%82%82%E3%81%82%E3%82%8B
# (これを見てたおかげですぐわかった)
