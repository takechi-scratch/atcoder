N = int(input())
hands = [input().split() for _ in range(N)]

ans = 0
for i in range(N - 1):
    if hands[i][1] == hands[i + 1][0]:
        ans += 1

print(ans)
