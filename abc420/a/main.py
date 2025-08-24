# N = int(input())
X, Y = [int(x) for x in input().split()]
print((X + Y - 1) % 12 + 1)
