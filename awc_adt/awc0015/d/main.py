N, M, C = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

ans = 0
for ok in reversed(A):
    while len(B) > 0 and B[-1] > ok:
        B.pop()

    if len(B) == 0:
        break

    ans += 1
    B.pop()

print(ans * C)
