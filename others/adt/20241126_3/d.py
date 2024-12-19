# https://atcoder.jp/contests/abc219/tasks/abc219_b

string = [input() for _ in range(3)]
sizi = [int(x) - 1 for x in list(input())]

ans = []
for x in sizi:
    ans.append(string[x])

print("".join(ans))
