N, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
new_A = []
target = min(A)


for x in A:
    new_x = x - T * ((x - target) // T)
    if abs(new_x - target) < abs(new_x - T - target):
        new_A.append(new_x)
    else:
        new_A.append(new_x - T)

A = new_A
A.sort()

score = A[-1] - A[0]
for i in range(N - 1):
    score = min(score, A[i] - (A[i + 1] - T))

print((score + 1) // 2)
