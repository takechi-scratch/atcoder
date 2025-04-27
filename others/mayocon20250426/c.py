N = int(input())
S = input()
W = [int(x) for x in input().split()]

people = list(zip(W, S))
people.sort()

now_ans = 0
for x in people:
    if x[1] == "1":
        now_ans += 1

ans = now_ans
now_ans = ans
for i in range(N):
    if people[i][1] == "0":
        now_ans += 1
    else:
        now_ans -= 1

    if i < N - 1 and people[i][0] == people[i + 1][0]:
        continue

    ans = max(ans, now_ans)

ans = max(ans, now_ans)
print(ans)
