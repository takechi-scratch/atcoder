N = int(input())
V = [int(x) for x in input().split()]
V.sort()
print(sum(V[i + 1] - V[i] for i in range(N - 1)))
