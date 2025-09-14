# 「求める答えを式で書く」→「展開して、前計算で必要な情報を取り出す」
# この考え方を忘れないこと。

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# jを決めたとき、Ajの係数は
# (j - Li + 1)(Ri - j + 1)

j_2_Aj_sum = [0]
for i, x in enumerate(A):
    j_2_Aj_sum.append(j_2_Aj_sum[-1] + (i + 1) ** 2 * x)

j_Aj_sum = [0]
for i, x in enumerate(A):
    j_Aj_sum.append(j_Aj_sum[-1] + (i + 1) * x)

Aj_sum = [0]
for x in A:
    Aj_sum.append(Aj_sum[-1] + x)


for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    j_2_Aj = j_2_Aj_sum[R] - j_2_Aj_sum[L - 1]
    j_Aj = j_Aj_sum[R] - j_Aj_sum[L - 1]
    Aj = Aj_sum[R] - Aj_sum[L - 1]
    print(-j_2_Aj + (L + R) * j_Aj - (L - 1) * (R + 1) * Aj)
