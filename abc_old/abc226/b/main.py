# 重複した要素を持たないsetが便利！

N = int(input())
ans = set()

for _ in range(N):
    # 入力をそのままsetにぶち込む（実は[1:]を消して、数列の長さも合わせて入れてもOK）
    ans.add(tuple(int(x) for x in input().split()[1:]))

print(len(ans))
