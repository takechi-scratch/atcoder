N = int(input())
S = input()
T = input()

win = 0
lose = 0
for i, j in zip(S, T):
    if i == "R":
        if j == "R":
            pass
        else:
            lose += 1
    else:
        if j == "R":
            lose += 1
        else:
            win += 1

print(win, lose)
