N = int(input())
S = list(input())
Q = int(input())

is_upper = [x.isupper() for x in S]
last_changed = [-1] * N
all_upper = -1
last_all_changed = -1

for i in range(Q):
    t, x, c = input().split()
    t, x = int(t), int(x) - 1

    if t == 1:
        S[x] = c
        last_changed[x] = i
        is_upper[x] = c.isupper()

    if t == 2:
        all_upper = 0
        last_all_changed = i

    if t == 3:
        all_upper = 1
        last_all_changed = i

ans = []
for i in range(N):
    if last_changed[i] >= last_all_changed:
        ans.append(S[i])

    elif all_upper == 1:
        ans.append(S[i].upper())

    else:
        ans.append(S[i].lower())

print("".join(ans))
