# 指示通りやるだけ（計算量は心配ない）

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

for x in B:
    if x in A:
        A.remove(x)

print(*A)
