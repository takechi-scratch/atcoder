M = 23
MOD = 10007


x = 0
for i in range(10000):
    x = x * 10 + 1
    print((x // M) % MOD, x % M)
