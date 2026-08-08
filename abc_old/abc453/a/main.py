N = int(input())
S = input()

ok = 0
while ok < N:
    if S[ok] == "o":
        ok += 1
    else:
        break

print(S[ok:])
