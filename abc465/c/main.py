N = int(input())
S = input()

head = []
tail = []
is_head = False
for i in range(N - 1, -1, -1):
    if S[i] == "o":
        is_head = not is_head

    if is_head:
        head.append(i)
    else:
        tail.append(i)

print(*[i + 1 for i in head + list(reversed(tail))])
