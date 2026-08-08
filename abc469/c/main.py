from bisect import bisect_right

N = int(input())
S = input()

x_pos = [i for i, x in enumerate(S) if x == "x"]
ans = []
stocks = 0
for i in range(N):
    if S[i] == "o":
        stocks += 1

    x_count = bisect_right(x_pos, i) + stocks
    if x_count > len(x_pos):
        ans.append(N)
    else:
        ans.append(x_pos[x_count - 1] + 1)

print(*ans, sep="\n")
