from math import isqrt

N = int(input())
ans = set()
ans_all = set()

for y in range(1, isqrt(N) + 2):
    for x in range(1, y):
        num = x ** 2 + y ** 2

        if num > N:
            continue

        if num in ans_all:
            ans.discard(num)
            continue

        ans.add(num)
        ans_all.add(num)

print(len(ans))
print(" ".join(str(x) for x in sorted(ans)))
