N, M = [int(x) for x in input().split()]
X = [int(x) - 1 for x in input().split()]
A = [int(x) for x in input().split()]

# 合計があっていない場合はアウト。ここはできてた！
if sum(A) != N:
    print(-1)
    exit()

# WAポイント！入力がソートされているかしっかり確認する。
# かなりの参加者が見落としがちだったらしい。
li = (sorted(list(zip(X, A)), key=lambda x: x[0]))

sum_stones = 0
for x in reversed(li):
    sum_stones += x[1]
    if sum_stones > N - x[0]:
        print(-1)
        exit()


# 合計はこれで簡単に計算できる！
now_score = sum(x * y for x, y in li)
print(N * (N - 1) // 2 - now_score)
