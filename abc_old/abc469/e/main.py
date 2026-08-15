N, K = [int(x) for x in input().split()]
S = input()

ok, ng = 0.0, 1.0
while ng - ok < 10**-7:
    rate = (ok + ng) / 2
    A = [1 - rate if x == "o" else -rate for x in S]
    # Aの中で、任意の区間をとってその和が0以上ならばOK
