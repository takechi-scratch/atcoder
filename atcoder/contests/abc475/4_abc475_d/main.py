from math import isqrt

S = input()

prime = []
prime_check = [True] * (10**7)
prime_check[0] = False
prime_check[1] = False
for i in range(2, len(prime_check)):
    if prime_check[i]:
        prime.append(i)
        if i > isqrt(len(prime_check)) + 10:
            continue

        for k in range(2 * i, len(prime_check), i):
            prime_check[k] = False

for p in prime:
    x = str(p)
    if len(x) != len(S):
        continue

    a = {}
    ok = True
    for key, num in zip(S, x):
        if key not in a:
            a[key] = num
        else:
            if a[key] != num:
                ok = False
                break

    if ok and len(a.values()) == len(set(a.values())):
        print(p)
        break

else:
    print(-1)
