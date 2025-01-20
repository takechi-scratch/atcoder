# 最大ケースで20秒弱くらい。C++に翻訳してもらったら1.7秒程度になりました。

from math import sqrt, floor

N = int(input())
root_max = floor(sqrt(N))
ans = 0

for i in range(1, root_max + 1):
    # ルートの中身も平方数ならアウト
    if sqrt(i) % 1 == 0:
        continue

    # ルートの中身が2つの素数の積で表せるかどうかを確認
    # 素数のリストを先に作っておくべきかも
    for j in range(2, floor(sqrt(i)) + 1):
        if i % j == 0:
            test = i // j
            last = j
            break
    else:
        continue

    for j in range(last, floor(sqrt(i)) + 1):
        if test % j == 0:
            break
    else:
        # print(i ** 2)
        ans += 1

# WAポイント！i**8のケースを忘れないこと。
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 57]
for i in prime:
    if i ** 8 <= N:
        ans += 1
    else:
        break

print(ans)
