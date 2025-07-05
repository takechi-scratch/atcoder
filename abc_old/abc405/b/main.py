# 愚直に毎回計算して間に合う

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

while True:
    mada = set(range(1, M + 1))
    for x in A:
        mada.discard(x)

    if len(mada) > 0:
        print(N - len(A))
        break

    A.pop()

else:
    print(N)
