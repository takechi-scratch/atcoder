# https://atcoder.jp/contests/abc245/tasks/abc245_b

N = int(input())
A = set(int(x) for x in input().split())

for ans in range(2005):
    if ans not in A:
        break

print(ans)
