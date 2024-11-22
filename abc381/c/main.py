# 惜しかったポイント→問題文をよく読む！！！
# 部分文字列が連続しているか連続していないか。

N = int(input())
S = input()

ans = 0
a = 0
b = 0
collecting = "1"

for i in range(N):
    # 1モードで1が来れば増やす
    if S[i] == "1" and collecting == "1":
        a += 1

    elif S[i] == "2" and collecting == "2":
        b += 1

    # 1モードでスラッシュが来れば2モードに変える
    elif S[i] == "/" and collecting == "1":
        collecting = "2"

    # それ以外ならアウト、集計に
    else:
        ans = max(ans, min(a, b))
        a = 0
        b = 0
        collecting = "1"

        # 下のポイントと同じく気を付ける。
        if S[i] == "1":
            a += 1

# WAポイント！集計がfor文の中だけになっていないか。
# 集計される前にループを抜ける恐れがあるので要確認。
ans = max(ans, min(a, b))
print(ans * 2 + 1)
