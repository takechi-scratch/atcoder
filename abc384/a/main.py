N, c1, c2 = input().split()
S = list(input())
# リストに変えてから1文字ずつチェック（焦ってenumerate使ってる人↓）
ans = []
for i, x in enumerate(S):
    if x != c1:
        ans.append(c2)
    else:
        ans.append(x)

print("".join(ans))
