N = int(input())
ans = []
str_count = 0
for _ in range(N):
    c, l = input().split()
    l = int(l)
    str_count += l
    if str_count > 100:
        print("Too Long")
        exit()

    ans.append(c * l)

print("".join(ans))
