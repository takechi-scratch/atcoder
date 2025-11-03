# 指示通りやるだけ（-Bだとエラーになるらしい）

N, A, B = [int(x) for x in input().split()]
S = input()
print(S[A:N - B])
