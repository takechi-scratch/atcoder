# TLE解答。サンプルは通過。
# 整数の繰り上がり部分で二重ループになってるみたい？
# 整数計算だとなぜかREなので謎。要再検証。

N = int(input())
S = [int(x) for x in list(input())]

ketalist = [[] for _ in range(N + 10)]

for i, num in enumerate(S):
    cnt, sum_end = i + 1, N - i
    kekka = str(num) * sum_end
    for j in range(len(kekka)-1, -1, -1):
        ketalist[j] += [int(kekka[j])] * cnt

isOK = False

for i in range(N + 10):
    if isOK:
        ketalist[i] = ""
        continue

    sum_temp = sum(ketalist[i])
    if sum_temp > 10:
        ketalist[i + 1].append(sum_temp // 10)
    elif ketalist[i + 1] == []:
        isOK = True

    ketalist[i] = str(sum_temp % 10)

print("".join(reversed(ketalist)))
