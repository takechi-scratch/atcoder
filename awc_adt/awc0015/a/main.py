A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(sum(A[i] * B[i] for i in range(7)))
