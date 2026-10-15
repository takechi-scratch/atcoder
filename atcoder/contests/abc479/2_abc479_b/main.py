N = int(input())
S = input()

ans = 0
for i in range(1, 105):
    if "R" * i in S:
        ans = i

print(ans)
