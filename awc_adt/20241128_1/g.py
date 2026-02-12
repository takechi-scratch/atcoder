# https://atcoder.jp/contests/abc367/tasks/abc367_d
# ずっと解きたかった緑diff！！（解説ACではあるが）

from collections import deque

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# 円形のやつは2周回すのがポイント！
# ポイント：累積和と余り
# ～～の倍数ときたら、余りを取って一致する箇所を数えるのが良い。

sum_steps = [0]
for i in range(N * 2):
    sum_steps.append((sum_steps[-1] + A[i % N]) % M)

ans = 0
steps_dict = {}
for i, mod in enumerate(sum_steps):
    # 出し入れすることを考えてdictにdequeを入れる形に
    if mod not in steps_dict:
        steps_dict[mod] = deque()
    steps_dict[mod].append(i)

    # 2周回った分、1周を超えているものがあれば削除
    # WAポイント！条件にイコールが入るか入らないか要確認。
    while len(steps_dict[mod]) >= 2 and i - steps_dict[mod][0] >= N:
        steps_dict[mod].popleft()

    # 2周目以降に答えのカウントを始めるのがポイント！！
    # 2周目→1周目と、2周目→1周目でカバーできる。
    if i > N and len(steps_dict[mod]) >= 2:
        ans += len(steps_dict[mod]) - 1

    # ちなみに、にぶたんやったらTLEでした
    # if i > N:
    #     ans -= len(steps_dict[mod]) - bisect_left(steps_dict[mod], N) - 1

print(ans)
