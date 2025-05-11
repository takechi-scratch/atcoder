# テンプレコード、グラフのテストケース生成

from random import randint
N = randint(1, 10)
M = randint(0, min(100, N * (N - 1) // 2))

sides = set()
while len(sides) < M:
    u, v = randint(1, N), randint(1, N)
    if u >= v:
        continue
    if (u, v) in sides:
        continue

    sides.add((u, v))

print(N, M)
print("\n".join([f"{u} {v}" for u, v in sides]))
