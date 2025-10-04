T, M = [int(x) for x in input().split()]

testcases = []
for _ in range(T):
    N = int(input())
    C = [int(x) for x in input().split()]
    testcases.append([N, C])

max_C = max(sum(C) for _, C in testcases)
# print(max_C)

# 組み合わせの計算はこの漸化式でできる！！（数学でやったやつ）
# 非素数modでも、nが小さければ使える。
comb = [[0] * (max_C + 1) for _ in range(max_C + 1)]
for n in range(1, max_C + 1):
    for k in range(max_C + 1):
        if n < k:
            continue

        if n == 1:
            comb[n][k] = 1
        elif k == 0:
            comb[n][k] = 1
        else:
            comb[n][k] = (comb[n - 1][k] + comb[n - 1][k - 1]) % M

# print(comb[5][2])
# assert comb[5][2] == 10

for N, C in testcases:
    sum_C = sum(C)
    ans = 1
    for x in C:
        ans *= comb[sum_C][x]
        ans %= M
        sum_C -= x

    print(ans)
