P, Q = [int(x) for x in input().split()]
A, B = [int(x) for x in input().split()]

print(min(Q, P) * A + max(Q - P, 0) * B)
