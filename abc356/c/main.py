N, M, K = [int(x) for x in input().split()]
test_keys = []
test_results = []

# 入力がちょっとトリッキーかも
for i in range(M):
    temp = input().split()
    kazu = int(temp[0])
    test_keys.append([int(x) for x in temp[1:1+kazu]])
    test_results.append(temp[-1])

# 自作ライブラリ ビット全探索の候補を生成
bits = []
for i in range(2 ** N):
    bit = list(bin(i)[2:])
    bit = [0] * (N - len(bit)) + [int(x) for x in bit]
    bits.append(bit)

ans = 0
for pattern in bits:
    # 愚直な2重ループでOK！
    for i, test_key in enumerate(test_keys):
        ok_key = 0
        for key in test_key:
            if pattern[key - 1]:
                ok_key += 1

        if ok_key >= K and test_results[i] == "x":
            break
        if ok_key < K and test_results[i] == "o":
            break

    else:
        ans += 1

print(ans)
