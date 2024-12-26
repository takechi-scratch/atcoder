# WA解法。週の端同士にあるものを判定できない？

N, A, B = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

for i, x in enumerate(D):
    # あまりだけ考える
    D[i] = x % (A + B)
    # いわゆる「2周する」ってやつ
    # if D[i] > (A + B) // 2:
    #     D[i] -= A + B

D.sort()
print("Yes" if D[-1] - D[0] < A else "No")
