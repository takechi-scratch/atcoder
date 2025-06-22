# 愚直にやると、文字列操作を考える結果2乗オーダーになってしまう
# 「どのPCの編集が最終結果に影響するか？」を確認するために、逆から見る

N, Q = [int(x) for x in input().split()]
queries = []
for _ in range(Q):
    queries.append(input().split())

ans = []
having_pc = -1
for query in reversed(queries):
    if query[0] == "3" and having_pc == -1:
        having_pc = int(query[1]) - 1

    elif query[0] == "2" and int(query[1]) - 1 == having_pc:
        ans.append(query[2])

    # WAポイント！条件をしっかりと確認。使っていない入力があったら、それはおかしい。
    # **having_pc == int(query[1]) - 1**も必要
    elif query[0] == "1" and having_pc == int(query[1]) - 1:
        having_pc = -1

print("".join(reversed(ans)))
