N, L, W = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]
print(len([x for x in D if L - W <= x <= L + W]))
