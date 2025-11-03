N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = [int(x) for x in input().split()]
    X.append(x)
    Y.append(y)

# 「X座標が一番遠い組の距離」と「Y座標が一番遠い組の距離」
# のうち、長い方は絶対必要。その分だけ取っておけば、あとは良い感じのところで集まれる。
print((max(max(X) - min(X), max(Y) - min(Y)) + 1) // 2)
