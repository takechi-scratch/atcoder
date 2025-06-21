N = int(input())
D = [int(x) for x in input().split()]

ans = [D[0]]
for i in range(1, N - 1):
    ans.append(ans[-1] + D[i])

print(*ans, sep=" ")

for i in range(N - 2):
    ans.pop(0)
    ans = [x - D[i] for x in ans]
    print(*ans, sep=" ")
