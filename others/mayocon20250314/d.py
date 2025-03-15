from bisect import bisect_right

N, M = [int(x) for x in input().split()]

# https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

l = make_divisors(M)
print(l[bisect_right(l, min(N, M // N)) - 1])
