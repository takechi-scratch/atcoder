N = int(input())
A = [int(x) for x in input().split()]

for i in range(N - 1):
    if A[i] >= A[i + 1]:
        print("No")
        exit()
else:
    print("Yes")
