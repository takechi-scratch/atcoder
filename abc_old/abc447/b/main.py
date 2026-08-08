S = input()
max_count = 0
for x in S:
    max_count = max(max_count, S.count(x))

for x in S:
    if S.count(x) == max_count:
        S = S.replace(x, "")

print(S)
