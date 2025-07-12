# 10進法でできる回文はそこまで多くないので列挙してしまう

from itertools import product

def convert_from_10(x: int, base: int):
    """10進数からN進数への変換（進法変換）"""

    ans = []
    while x > 0:
        ans.append(str(x % base))
        x //= base

    return "".join(reversed(ans))

A = int(input())
N = int(input())
ans = 0

for keta_num in range(1, 13):
    need_nums = (keta_num + 1) // 2
    for comb in product("0123456789", repeat=need_nums):
        if comb[0] == "0":
            continue

        x_raw = []
        x_raw.extend(comb)
        if keta_num % 2 != 0:
            x_raw.pop()
        x_raw.extend(reversed(comb))

        x = int("".join(x_raw))
        if x > N:
            continue

        x_A = convert_from_10(x, A)
        for i in range(len(x_A)):
            if x_A[i] != x_A[len(x_A) - i - 1]:
                break

        else:
            # print(x)
            ans += x

print(ans)
