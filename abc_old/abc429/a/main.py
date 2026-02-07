N, M = [int(x) for x in input().split()]
print(*["OK" if i < M else "Too Many Requests" for i in range(N)], sep="\n")
