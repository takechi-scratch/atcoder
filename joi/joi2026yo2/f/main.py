N = int(input())
A = [int(x) for x in input().split()]

if N % 2 == 0:
    print(min(A[i + N // 2] - A[i] for i in range(N // 2)))
    exit()

# 奇数の場合はどうなる？
