# 2進数に置き換えて考えることができる！

N, X = [int(x) for x in input().split()]
S = list(input())

now = list(bin(X)[2:])
for query in S:
    if query == "U":
        now.pop()

    elif query == "L":
        now.append("0")

    elif query == "R":
        now.append("1")

print(int("".join(now), 2))
