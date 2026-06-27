A = 525950964

for i in range(1, 1000000):
    if A * i % 998244353 < 1000:
        print(i, A * i % 998244353)
