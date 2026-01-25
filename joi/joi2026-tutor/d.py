N = int(input())
target = [[int(x) for x in input().split()] for _ in range(N)]

ans = 10 ** 18
ans_x, ans_y = -1, -1
for i in range(10):
    for j in range(10):
        now_ans = 0
        for x, y in target:
            now_ans += abs(x - i) + abs(y - j)
        if ans > now_ans:
            ans = now_ans
            ans_x = i
            ans_y = j

print(ans_x, ans_y)
