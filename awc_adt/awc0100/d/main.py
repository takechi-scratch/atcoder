N = int(input())
A = [int(x) for x in input().split()]
group_A = 0
group_B = sum(A)
ans = group_B
for x in A[: N - 1]:
    group_A += x
    group_B -= x
    ans = min(ans, abs(group_A - group_B))

print(ans)
