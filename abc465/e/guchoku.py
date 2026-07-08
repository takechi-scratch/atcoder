N = int(input())

ans = 0
for i in range(1, N + 1):
    count = int(i % 3 == 0)
    if "3" in str(i):
        count += 1
    if len(set(str(i))) == 3:
        count += 1

    ans += count > 0

print(ans)
