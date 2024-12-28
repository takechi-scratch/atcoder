K = int(input())
S = input()
T = input()

if len(S) - len(T) == 0:
    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1
            if diff >= 2:
                break

    if diff <= 1:
        print("Yes")
    else:
        print("No")


elif abs(len(S) - len(T)) == 1:
    if len(S) > len(T):
        # WAポイント！！文字のスワップは丁寧に。
        temp = T
        T = S
        S = temp

    diff = 0
    for i in range(len(T)):
        if i >= len(T) - 1 and diff == 0:
            diff += 1
            break

        if S[i - diff] != T[i]:
            diff += 1
            if diff >= 2:
                break

    if diff <= 1:
        print("Yes")
    else:
        print("No")


else:
    print("No")
