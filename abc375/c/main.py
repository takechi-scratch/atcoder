# TLE解答。

N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))

# 2次元配列の回転の関数は使えるかも。Pythonだとコードが楽。
def kaiten(list2d, degrees=1):
    degrees = degrees % 4
    if degrees == 1:
        list2d.reverse()
        # 行と列を転置する方法
        list2d = [list(x) for x in zip(*list2d)]
    elif degrees == 3:
        list2d = [list(x) for x in zip(*list2d)]
        list2d.reverse()
    elif degrees == 2:
        list2d.reverse()
        list2d = [reversed(x) for x in list2d]
    else:
        pass

    return list2d

# 結局は90度回転を何回かやるだけ。
for i in range(N // 2):
    kaiten_results = kaiten([l[i:N-i] for l in A[i:N-i]])
    for j, result in enumerate(kaiten_results):
        A[i + j][i:N-i] = result

for ans in A:
    print("".join(ans))

"""
見直すべきポイント
回転を何度もやると遅くなるので、少なくするべき？
はじめに4回転分作っておいて、座標に応じて選ぶのがGoodかな？
"""
