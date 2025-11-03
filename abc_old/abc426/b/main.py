S = list(input())
s_set = list(set(S))

print(s_set[0] if S.count(s_set[0]) <= 1 else s_set[1])
