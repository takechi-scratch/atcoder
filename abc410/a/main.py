N = int(input())
A = [int(x) for x in input().split()]
K = int(input())

print(len([x for x in A if x >= K]))
