S = [int(x) for x in input().split("-")]
# 後ろは+1したものを1~8の余りで表現（((S[1] + 1) - 1) % 8 + 1）
print(S[0] + 1 if S[1] == 8 else S[0], S[1] % 8 + 1, sep="-")
