N = int(input())
A = [int(x) for x in input().split()]

A.sort()
ans = []

if N % 2 == 0:
    now_ans = A[0] + A[-1]
    if all(A[i] + A[N - i - 1] == now_ans for i in range(N)):
        ans.append(now_ans)

if all(A[0] == A[i] for i in range(N)):
    ans.append(A[0])

A_max = A[-1]
while len(A) > 0 and A[-1] == A_max:
    A.pop()

NN = len(A)
if NN % 2 == 0 and NN > 0:
    now_ans = A[0] + A[-1]
    if all(A[i] + A[NN - i - 1] == now_ans for i in range(NN)):
        ans.append(now_ans)

print(*sorted(set(ans)))
