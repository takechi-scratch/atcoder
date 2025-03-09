N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print("Yes" if ans == 0 else "No")
