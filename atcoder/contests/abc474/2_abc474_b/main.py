from math import ceil

N = int(input())
P = [int(x) - 1 for x in input().split()]

ok = True
for i, x in enumerate(P):
    group = i // 10
    if not group * 10 <= x < (group + 1) * 10:
        ok = False
        break

print("Yes" if ok else "No")
