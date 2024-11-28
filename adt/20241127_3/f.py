# https://atcoder.jp/contests/abc234/tasks/abc234_c

K = int(input())

ans_kari = list(bin(K)[2:])
ans = "".join(["2" if x == "1" else "0" for x in ans_kari])
print(ans)
