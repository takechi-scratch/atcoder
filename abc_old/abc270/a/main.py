A, B = [int(x) for x in input().split()]
ans = 0
if A >= 4 or B >= 4:
    ans += 4
if A % 4 >= 2 or B % 4 >= 2:
    ans += 2
if A % 2 >= 1 or B % 2 >= 1:
    ans += 1

print(ans)
