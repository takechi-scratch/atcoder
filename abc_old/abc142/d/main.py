A, B = [int(x) for x in input().split()]

import subprocess

def prime_factorization(x: int) -> set[int]:
    out = subprocess.run(["factor", str(x)], stdout=subprocess.PIPE, check=True).stdout
    return set(int(x) for x in out.decode().strip().split(" ")[1:])

# それぞれ素因数分解して、共通するものの個数
# あとは1が足りないので足す
print(len(prime_factorization(A) & prime_factorization(B)) + 1)
