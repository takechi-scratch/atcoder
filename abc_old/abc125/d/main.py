# 操作の間で、マイナスの数が偶数か奇数かは変わらない
# 逆に、マイナスの数の偶奇性が変わらないパターンはなんでも実現できる

N = int(input())
A = [int(x) for x in input().split()]

A.sort(key=abs)

if len([x for x in A if x < 0]) % 2 == 0:
    print(sum([abs(x) for x in A]))
else:
    # マイナスを1つ残さなければいけない場合は、絶対値の一番小さいやつで
    print(sum([abs(x) for x in A]) - abs(A[0]) * 2)
