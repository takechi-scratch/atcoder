# ふつうに2乗ループを回しても全く問題ない

H, W, N = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]
B = [int(input()) for _ in range(N)]

print(max(len([y for y in x if y in B]) for x in A))
