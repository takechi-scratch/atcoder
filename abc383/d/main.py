from math import sqrt, floor, comb

N = int(input())
root_max = floor(sqrt(N)) + 1
primes = set([2])

for i in range(3, floor(sqrt(root_max)) + 1):
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.add(i)

print(comb(len(primes), 2))
