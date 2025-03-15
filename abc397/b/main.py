S = input()
before = len(S)

i = 0
while True:
    if i >= len(S):
        break

    if i % 2 == 1 and S[i] == "o":
        i += 1
        continue
    if i % 2 == 0 and S[i] == "i":
        i += 1
        continue

    add = "o" if i % 2 == 1 else "i"

    S = S[:i] + add + S[i:]
    i += 2

print(len(S) - before + len(S) % 2)
