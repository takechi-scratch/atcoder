# ADT出題済み。

N = int(input())
S = []
for _ in range(N):
    S.append(input())

# Sから2つ選んで繰り返す
for i in range(N):
    for j in range(N):
        if i == j:
            # 同じものはくっつけられない
            continue

        # くっつける
        test = S[i] + S[j]

        # Kを長さの半分にする、奇数の場合は切り捨てるので真ん中の文字は見ないことになる
        for k in range(len(test) // 2 + 1):
            # 前からK番目、後ろからK番目の文字を比較
            if test[k] != test[-1 * k - 1]:
                break
        else:  # 最後までbreakされなかったとき
            print("Yes")
            exit()

# exitされずにチェックが終わってしまったときはNo
print("No")
