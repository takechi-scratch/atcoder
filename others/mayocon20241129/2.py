# https://atcoder.jp/contests/abc269/tasks/abc269_c

N = bin(int(input()))[2:]

ok_bit = []
for i in range(len(N)):
    if N[i] == "1":
        ok_bit.append(i)

for perm in range(2 ** len(ok_bit)):
    perm_b = bin(perm)[2:]
    perm_b = "0" * (len(ok_bit) - len(perm_b)) + perm_b
    ans = ["0"] * len(N)

    for i, bit in enumerate(perm_b):
        if bit == "1":
            ans[ok_bit[i]] = "1"

    print(int("".join(ans), 2))
