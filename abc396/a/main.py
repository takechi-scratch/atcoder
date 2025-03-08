N = int(input())
A = [int(x) for x in input().split()]

for i in range(N - 2):
    if A[i] == A[i + 1] == A[i + 2]:
        print("Yes")
        exit()
else:
    print("No")
