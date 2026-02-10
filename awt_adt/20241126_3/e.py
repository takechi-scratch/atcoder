# https://atcoder.jp/contests/abc216/tasks/abc216_c

N = int(input())
ans = []

while N > 1:
    if N % 2 == 0:
        ans.append("B")
        N = N // 2
    else:
        ans.append("A")
        N -= 1

ans.append("A")
print("".join(reversed(ans)))
