# 再帰は苦手だったかな。

# テンプレコード 再帰を利用する際の上限緩和
import sys
sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]

base = []
for i in range(N):
    base.append(1 + 10 * i)

plus_max = M - base[-1]
ans = []

# どこまでが自由に動かせるかを引数にしておく
def generate(base, free):
    if free == 0:
        ans.append([str(x) for x in base])
        return

    # 操作するやつがどこまで進んでいいか
    free_to = M - 10 * (free - 1)
    # WAポイント！リスト外参照注意。今回は端だけ例外にしてる。
    if free == N:
        start = base[-1 * free]
    else:
        # スタートが前の数字+10から
        start = base[-1 * free - 1] + 10
    for i in range(start, free_to + 1):
        if free == 1:
            generate(base[:-1 * free] + [i], free - 1)
        else:
            # 一番最後の部分は別になくてもいいから、省くような実装も作りたい
            generate(base[:-1 * free] + [i] + base[-1 * free + 1:], free - 1)

generate(base, N)
print(len(ans))
print("\n".join([" ".join(x) for x in ans]))
