# indexをプラスしたものとマイナスしたものに興味がありそう...→試す
# プラスのものと、マイナスのものを1個ずつ選んで、和が0になったらカウント。

from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]

# 1コずつ試すのではなく、Counterでまとめた後に個数を比較して掛け算している。
A_plus = Counter([x + i + 1 for i, x in enumerate(A)])
A_minus = Counter([x - (i + 1) for i, x in enumerate(A)])

ans = 0
for x in A_plus.keys():
    ans += A_plus[x] * A_minus[-x]

print(ans)
