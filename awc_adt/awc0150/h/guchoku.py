from itertools import permutations

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = 0
for narabi in permutations(range(N), N):
    sukima = [abs(A[narabi[i + 1]] - A[narabi[i]]) for i in range(N - 1)]
    sukima.sort(reverse=True)
    ans = max(ans, sum(sukima[:K]))
    if ans == 198:
        print([A[narabi[i]] for i in range(N)])
        break

print(ans)
