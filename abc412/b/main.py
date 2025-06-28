S = input()
T = input()

for i in range(1, len(S)):
    if S[i].isupper() and S[i - 1] not in T:
        print("No")
        exit()

else:
    print("Yes")
