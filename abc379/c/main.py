# WA解答。後ろから見ていっているのが良くない？

N, M = [int(x) for x in input().split()]
X = [int(x) - 1 for x in input().split()]
A = [int(x) for x in input().split()]

def solve():
    # 合計があっていない場合はアウト。ここはできてた！
    if sum(A) != N:
        print(-1)
        return

    # WAポイント！入力がソートされているかしっかり確認する。
    # かなりの参加者が見落としがちだったらしい。
    li = (sorted(list(zip(X, A)), key=lambda x: x[0]))
    # print(li)

    ans = 0
    w_boxes = 0
    bef_i = N

    # 後ろから見るときのforループは-1を連打。テンプレコード
    for i in range(M-1, -1, -1):
        w_boxes += bef_i - li[i][0] - 1

        if w_boxes < li[i][1] - 1:
            print(-1)
            return

        # 元から石が置かれてる場所をまたぐときの処理も考えないといけない。
        ans += (w_boxes + 1) * w_boxes // 2

        w_boxes -= li[i][1] - 1
        bef_i = li[i][0]


    print(ans)


solve()
