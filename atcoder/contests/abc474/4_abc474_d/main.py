N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

if all(x <= y for x, y in zip(A, B)):
    print("No")
else:
    ans = [1] * N
    for i in range(N):
        if A[i] > B[i]:
            ans[i] = 10**18
            break

    print("Yes")
    print(*ans, sep=" ")
