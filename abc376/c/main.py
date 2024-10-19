N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

b_cnt = N - 1
ans = -2

for a_cnt in range(N-1, -1, -1):
    if len(B) == 0:
        ans = A[a_cnt]
        continue

    if B[-1] < A[a_cnt]:
        if ans != -2:
            ans = -1
            break
        else:
            ans = A[a_cnt]
            continue


    B.pop(-1)

print(ans)
