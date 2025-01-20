S = input()
cnt = 0
for i in range(1, len(S)):
    if S[i] == "-":
        cnt += 1
    else:
        if i == len(S) -1:
            print(cnt)
        else:
            print(cnt, end=" ")
        cnt = 0
