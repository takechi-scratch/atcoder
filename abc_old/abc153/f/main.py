# （半）解説AC。しゃくとり法が思いつかなかったかも

N, D, A = [int(x) for x in input().split()]

monsters = []
for _ in range(N):
    x, h = [int(x) for x in input().split()]
    monsters.append((x, h))

monsters.sort()

# 「ここより左まで当たった」爆弾の個数（ここ含む）
bomb_count = [0] * N
# 今当たっているところにあらかじめ爆弾が当たった回数を記録
now_bombs = 0

ans = 0
cur = 1
for i, monster in enumerate(monsters):
    pos, hp = monster
    need_bombs = max(0, (hp - 1) // A + 1 - now_bombs)
    ans += need_bombs
    # 足す
    now_bombs += need_bombs

    # しゃくとり法。どこまで爆弾が当たるか更新（curはギリギリ当たらないところ）
    while cur < N and pos + 2 * D >= monsters[cur][0]:
        cur += 1

    bomb_count[cur - 1] += need_bombs
    # それより右には bomb_count[i] 個の爆弾が当たってないから引く
    now_bombs -= bomb_count[i]

print(ans)