N = int(input())
C = [int(x) for x in input().split()]

for i in range(N):
    ans = 0
    for j in range(N):
        if i == j:
            continue

        if C[i] == C[j]:
            ans += max(i - j, j - i)

    print(ans)
