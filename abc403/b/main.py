from itertools import permutations

T = list(input())
U = list(input())

for add in permutations("abcdefghijklmnopqrstuvwxyz", 4):
    now_T = T.copy()
    used = 0
    for i, x in enumerate(now_T):
        if x == "?":
            now_T[i] = add[used]
            used += 1

    appeared = 0
    for i in range(len(T)):
        if now_T[i] == U[appeared]:
            appeared += 1

        else:
            appeared = 0

        if appeared == len(U):
            # print(now_T)
            print("Yes")
            exit()


print("No")
