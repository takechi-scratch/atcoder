from sys import stderr

N, M, L = [int(x) for x in input().split()]
love_str = []
for _ in range(N):
    s, p = input().split()
    love_str.append((s, int(p)))

priority_scores = [[0] * 6 for _ in range(6)]
for s, p in love_str:
    for i in range(len(s ) - 1):
        priority_scores[ord(s[i]) - 97][ord(s[i + 1]) - 97] += p

for i in range(6):
    ans = []
    sum_score = sum(priority_scores[i])
    for j in range(6):
        ans.append(priority_scores[i][j] * 100 // sum_score)

    ans[5] += 100 - sum(ans)
    print(chr(97 + i), *ans, "0 0 0 0 0 0")
    print(f"{sum(ans) = }", file=stderr)

print("a 100 0 0 0 0 0 0 0 0 0 0 0\n" * 6, end="")
