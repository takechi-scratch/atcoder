from itertools import combinations_with_replacement

N, M, Q = [int(x) for x in input().split()]
options = []
for _ in range(Q):
    options.append(tuple(int(x) for x in input().split()))

ans = 0
# itertoolsは便利！！（重複組み合わせを列挙してくれる。手で実装すると枝刈りが面倒）
for raw_x in combinations_with_replacement(range(M), N):
    A = list(raw_x)
    A.sort()

    now_ans = 0
    for x in options:
        if A[x[1] - 1] - A[x[0] - 1] == x[2]:
            now_ans += x[3]

    ans = max(ans, now_ans)

print(ans)
