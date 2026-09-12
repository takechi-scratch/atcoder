N = int(input())
A = [int(x) for x in input().split()]
target = max(A)

B = [None] * N
ok = True
for i in range(N - 1, -1, -1):
    now_sum = 0
    for k in reversed(range(i, N, i + 1)):
        if k == i:
            break

        now_sum += B[k]

    if target - (A[i] + now_sum) < 0:
        ok = False
        break
    else:
        B[i] = target - (A[i] + now_sum)

if ok:
    print(sum(B))
else:
    print(-1)
