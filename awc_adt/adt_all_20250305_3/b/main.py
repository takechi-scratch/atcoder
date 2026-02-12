# https://atcoder.jp/contests/abc248/tasks/abc248_a

S = input()
l = list(range(10))

for x in S:
    l.remove(int(x))

print(l[0])
