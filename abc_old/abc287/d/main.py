S = list(input())
T = list(input())
len_s, len_t = len(S), len(T)

ok = [False] * len_t
ng_count = 0

for i in range(len_t):
    if S[len_s - len_t + i] == "?":
        ok[i] = True
    elif T[i] == "?":
        ok[i] = True
    elif S[len_s - len_t + i] == T[i]:
        ok[i] = True
    else:
        ok[i] = False
        ng_count += 1

ans = []
for i in range(len_t + 1):
    assert ng_count >= 0
    ans.append("Yes" if ng_count == 0 else "No")

    if i == len_t:
        continue

    bef_ok = ok[i]
    if S[i] == "?":
        ok[i] = True
    elif T[i] == "?":
        ok[i] = True
    elif S[i] == T[i]:
        ok[i] = True
    else:
        ok[i] = False

    if not bef_ok and ok[i]:
        ng_count -= 1
    elif bef_ok and not ok[i]:
        ng_count += 1


print("\n".join(ans))
