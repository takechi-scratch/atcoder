N = int(input())
A = [int(x) for x in input().split()]

ans = [0] * (2 * 10**5 + 100)
for x in A:
    ans[0] += 1
    ans[x] -= 1

for i in range(len(ans)):
    if i > 0:
        ans[i] += ans[i - 1]

    if ans[i] == 0:
        continue

    ans[i + 1] += ans[i] // 10
    ans[i] %= 10

while ans[-1] == 0:
    ans.pop()

print("".join(str(x) for x in reversed(ans)))
