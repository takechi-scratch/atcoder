N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for i, x in enumerate(A):
    if x >= K:
        print(i + 1)
        break

else:
    print(-1)
