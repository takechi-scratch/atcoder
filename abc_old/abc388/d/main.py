# 成人祝い → 祝い成人、っていう問題らしい（？）

# 要素をずっとソートしておいてくれるライブラリ
from sortedcontainers import SortedList

N = int(input())
A = [int(x) for x in input().split()]
# それぞれの人が何年まで成人祝いをあげられるのか保管しておく
last_cangive = SortedList([])
ans = []

for i in range(N):
    # 成人祝いでもらえる石を計算
    get_stones = len(last_cangive) - last_cangive.bisect_left(i + 1)
    last_cangive.add(i + 1 + A[i] + get_stones)
    # 石を最後まであげ続けているとして、石が残っていたらその個数、
    # マイナスなら途中であげられなくなっているので0
    ans.append(max(0, A[i] + get_stones - (N - i - 1)))

# リストをまとめて出力するにはこれが便利だと知りました（printの引数に分割しながら渡してる感じ？）
print(*ans)
