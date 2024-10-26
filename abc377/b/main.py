data = []
for _ in range(8):
    data.append(list(input()))

# マスを1つずつ見て、大丈夫か確認
ans = 0
for i in range(8):
    if "#" in data[i]:
        continue

    for j in range(8):
        for k in range(8):
            if data[k][j] == "#":
                break
        else:
            ans += 1

print(ans)
