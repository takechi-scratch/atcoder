S = list(input())
T = list(input())

S_others = ["_"]
S_count = [0]

for x in S:
    if x == "A":
        S_count[-1] += 1
    else:
        S_others.append(x)
        S_count.append(0)

T_others = ["_"]
T_count = [0]

for x in T:
    if x == "A":
        T_count[-1] += 1
    else:
        T_others.append(x)
        T_count.append(0)

if S_others == T_others:
    print(sum(abs(x - y) for x, y in zip(S_count, T_count)))

else:
    print(-1)
