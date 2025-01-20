# https://atcoder.jp/contests/abc249/tasks/abc249_b
S = list(input())
lower, upper, different = False, False, True
# 一応setを使って高速化してみる
appeared = set()
for x in S:
    # テンプレコード、大文字と小文字の確認
    # 全ての文字が大文字or小文字だった場合にTrueになる
    lower = lower or x.islower()
    upper = upper or x.isupper()
    if x in appeared:
        different = False
    appeared.add(x)

print("Yes" if lower and upper and different else "No")
