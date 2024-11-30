N, D = [int(x) for x in input().split()]
A = list(input())
i = N - 1
while D > 0:
    if A[i] == "@":
        A[i] = "."
        D -= 1
    i -= 1

print("".join(A))
