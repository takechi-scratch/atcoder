N, K = [int(x) for x in input().split()]
A = []
for _ in range(N):
    A.append([int(x) for x in input().split()][1:])
C = [int(x) for x in input().split()]

K -= 1
for i in range(N):
    now_len = len(A[i]) * C[i]
    if K < now_len:
        print(A[i][K % len(A[i])])
        break
    K -= now_len
