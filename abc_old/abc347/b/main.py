S = input()

if len(S) == 1:
    print(1)
    exit()

ans = set()

for start in range(len(S)):
    for end in range(1, len(S) + 1):
        ans.add(S[start:end])

# print(ans)
print(len(ans) - 1)
