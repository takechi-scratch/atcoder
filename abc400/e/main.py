from math import isqrt
from bisect import bisect_right

Q = int(input())
query = [isqrt(int(input())) for _ in range(Q)]
max_query = max(query)

prime_max = int(isqrt(max_query))
prime_kouho = set(range(2, prime_max))
for i in range(2, isqrt(prime_max) + 1):
    if i not in prime_kouho:
        continue

    j = 2
    while i * j <= prime_max:
        prime_kouho.discard(i * j)
        j += 1

primes = list(sorted(prime_kouho))

fh_nums = []

# print(len(primes))
for i in range(len(primes)):
    i_pow = 1
    while True:
        a = primes[i] ** i_pow

        if a > max_query:
            break

        for j in range(i + 1, len(primes)):
            j_pow = 1
            while True:
                if a * (primes[j] ** j_pow) > max_query:
                    break

                fh_nums.append(a * (primes[j] ** j_pow))

                j_pow += 1

        i_pow += 1

fh_nums.sort()
# print(len(fh_nums))

for A in query:
    pos = bisect_right(fh_nums, int(A))
    print(fh_nums[pos - 1] ** 2)
