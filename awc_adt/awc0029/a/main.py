N, P, B, K = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
print(sum([(P + B) * x if x >= K else P * x for x in C]))
