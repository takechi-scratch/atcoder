import subprocess
from collections import Counter

def prime_factorization(x: int) -> list[int]:
  out = subprocess.run(["factor", str(x)], stdout=subprocess.PIPE, check=True).stdout
  return [int(x) for x in out.decode().strip().split(" ")[1:]]

N, P = [int(x) for x in input().split()]

# Pを素因数分解して、それぞれの約数の個数を見る
factor = Counter(prime_factorization(P))

ans = 1
for x, count in factor.items():
    # 約数がcount個だったとき、aそれぞれに(count // N)個割り当てることができる
    # その分だけ最大公約数も大きくなれる（均等に割り当てるのが最大だから）
    ans *= x ** (count // N)

print(ans)
