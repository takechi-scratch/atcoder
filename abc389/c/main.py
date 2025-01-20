Q = int(input())
# 今回は便宜的に頭の位置ではなく、長さを足した数をsnakeに格納している
snake = []
nukes = 0

for i in range(Q):
    query = input().split()

    if query[0] == "1":
        if len(snake) == 0:
            snake.append(int(query[1]))
        else:
            snake.append(snake[-1] + int(query[1]))

    elif query[0] == "2":
        # 抜けたとみなすことで、listでも問題を解ける
        # リストの先頭の要素を削除するのは遅いので、それをしたいなら
        # from collections import deque; snake = deque([])
        # という感じで、dequeを使う
        nukes += 1

    elif query[0] == "3":
        k = int(query[1])
        if k == 1:  # 一応例外として
            print(0)
        else:
            # 抜けた長さをシミュレート
            nuke_len = snake[nukes - 1] if nukes > 0 else 0
            print(snake[k + nukes - 2] - nuke_len)
