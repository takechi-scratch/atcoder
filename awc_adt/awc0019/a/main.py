N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(len([x for x in A if x >= K]))
