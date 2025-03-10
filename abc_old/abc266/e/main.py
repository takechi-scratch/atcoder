from math import floor

N = int(input())

ans = 3.5
for i in range(1, N):
    lows = floor(ans)
    ans = (lows * ans + (6 - lows) * (6.5 - (6 - lows) / 2)) / 6

print(ans)
