# 後日・解説AC

N, A, B = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

for i, x in enumerate(D):
    # あまりだけ考える
    D[i] = x % (A + B)

D.sort()

# 端だけ見てOK
if D[-1] - D[0] < A:
    print("Yes")
    exit()

for i in range(1, N):
    # 区切りをどこかに入れて、そのスタートから前（+1週間）での差でもチェック
    if D[i - 1] + (A + B) - D[i] < A:
        print("Yes")
        break
else:
    print("No")
