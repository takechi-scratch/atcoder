points = [int(x) for x in input().split()]
QUESTIONS = "ABCDE"

results = []
# 辞書順→最高位のbitが強い→降順にbitを並べる
for i in range(31, -1, -1):
    solved_raw = bin(i)[2:]
    # WAポイント！bitを並べるときは位揃えに注意
    solved = ["0"] * (5 - len(solved_raw)) + list(solved_raw)
    point = 0
    name = []
    for j in range(5):
        if solved[j] == "1":
            point += points[j]
            # nameは1文字ずつ生成
            name.append(QUESTIONS[j])

    name = "".join(name)

    results.append((point, name))

# 先にポイントで並べ替え、lambdaの使い方は要復習
results.sort(key=lambda x: x[0], reverse=True)
# 名前を取り出してリストを作り、結合
print("\n".join([x[1] for x in results]))

# 「空白が合わない！」っていってWAになってたけど、なんでだろう
