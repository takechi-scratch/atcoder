from bisect import bisect_right

ans = set()

a = [2 ** i for i in range(1, 10)]
b = [i ** 2 for i in range(1, 100)]

for i in a:
    for j in b:
        ans.add(i * j)

ans = list(sorted(ans))

with open("out.txt", "w") as f:
    for i in range(10000):
        print(bisect_right(ans, i), file=f)
