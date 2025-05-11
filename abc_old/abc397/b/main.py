# 前から見ていって、一致しない場所があったら書き足す

S = input()
before = len(S)

i = 0
while True:
    if i >= len(S):
        break

    if i % 2 == 1 and S[i] == "o":
        i += 1
        continue
    if i % 2 == 0 and S[i] == "i":
        i += 1
        continue

    add = "o" if i % 2 == 1 else "i"

    # 文字列の再生成は意外と計算量重め（O(N)?）だけど、
    # 長さは100までなので問題ない
    S = S[:i] + add + S[i:]

    # ループのインデックスに注意！
    # 足したあと、次は必ず問題ないので+2
    i += 2

print(len(S) - before + len(S) % 2)
