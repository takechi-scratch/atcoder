# 基本的にアンバランス度は1以下にできる。
# とりあえずBにすべて同じ数を入れ、残りはうまく1ずつ足していく
# 順番としては、2進法の0~2**Nをそれぞれひっくり返したindexに入れるとうまくいく。

N, K = [int(x) for x in input().split()]
Blen = 2 ** N
B = [K // Blen] * Blen

for i in range(K % Blen):
    stri = bin(i)[2:]
    stri = "0" * (N - len(stri)) + stri
    plus_index = int("".join(list(reversed(stri))), 2)
    B[plus_index] += 1

print(0 if K % Blen == 0 else 1)
print(*B)
