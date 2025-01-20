# https://atcoder.jp/contests/abc269/tasks/abc269_c

N = int(input())

N2 = bin(N)[2:]
omomi = []

for n in range(len(N2)-1, -1, -1):
    if N2[n] == "1":
        omomi.append(2 ** (len(N2) - n - 1))

omomi.reverse()

# bit全探索の方針で、各桁の重みを変える
for i in range(2 ** len(omomi)):
    mark = list(bin(i)[2:])
    ans = 0
    for j in range(-1, -1 * len(mark) - 1, -1):
        if mark[j] == "1":
            ans += omomi[j]

    print(ans)
