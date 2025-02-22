N = int(input())
S = []
for _ in range(N):
    S.append(input())

S.sort(key=len)
print("".join(S))
