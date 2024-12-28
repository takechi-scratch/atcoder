from math import ceil

S = input()
ans = 0
count_0 = 0

for i, x in enumerate(S):
    if x == "0":
        count_0 += 1
        continue

    if count_0 > 0:
        ans += ceil(count_0 / 2)
        count_0 = 0

    ans += 1

if count_0 > 0:
    ans += ceil(count_0 / 2)

print(ans)
