N = int(input())
login = False
ans = 0
for _ in range(N):
    sousa = input()
    if sousa == "login":
        login = True
    elif sousa == "logout":
        login = False
    elif sousa == "private" and not login:
        ans += 1

print(ans)
