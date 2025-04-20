# 全ての辺から2本選ぶ組み合わせ - 平行になる2本の組み合わせ

N, M = [int(x) for x in input().split()]
sides_count = [0] * N
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    # (a + b) % Nが一緒なら平行になる
    # いろいろ試してみると見えてくることが多い
    sides_count[(a + b) % N] += 1

ans = M * (M - 1) // 2
for x in sides_count:
    # 平行なものがx本ある場合、xC2通りの選び方だけ平行になる
    ans -= x * (x - 1) // 2

print(ans)
