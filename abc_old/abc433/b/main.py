N = int(input())
A = [int(x) for x in input().split()]

for i, x in enumerate(A):
    for j in range(i - 1, -1, -1):
        if A[j] > x:
            print(j + 1)
            break

    else:
        print(-1)
