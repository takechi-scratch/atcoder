# 円はやっぱり分かりづらいので、「ひらいてみる」ことが大切（気づいてた）あと、2周するテクはいらなそう
# 「交点があるか」ではなく、「交点がないか」を見てみる（視点を変える）

# セグ木は使わなくても大丈夫。

N = int(input())
Nodes = 2 * N
chords = [tuple(int(x) - 1 for x in input().split()) for _ in range(N)]
chord_to = [-1] * Nodes

for a, b in chords:
    chord_to[a] = b
    chord_to[b] = a

    if abs(a - b) % 2 == 0:
        print("Yes")
        exit()

stack = []
for i in range(Nodes):
    if len(stack) > 0 and stack[-1] == i:
        stack.pop()
        continue

    stack.append(chord_to[i])

if len(stack) == 0:
    print("No")
else:
    print("Yes")

# https://atcoder.jp/contests/abc394/tasks/abc394_d
# 「カラフル括弧列」みを感じた

# 9分ごろ実装開始
# 32:23 実装完了
# 38:54 デバッグ完了
# 39:41 提出(11WA)
# 47:16 休憩（嘘解法に気づく）
# 60:00 セグ木…？
# 79:03 答えを見てみる
