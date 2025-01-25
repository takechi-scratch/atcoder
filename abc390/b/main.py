N = int(input())
A = [int(x) for x in input().split()]

# if A[1] < A[0]:
#     A.reverse()

for i in range(1, N - 1):
    if A[i] * A[1] != A[i + 1] * A[0]:
        print("No")
        break

else:
    print("Yes")
