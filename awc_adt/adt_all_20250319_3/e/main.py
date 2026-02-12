# https://atcoder.jp/contests/abc323/tasks/abc323_c

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

now_scores = []

for i, x in enumerate(S):
    score = i + 1
    for j, status in enumerate(x):
        if status == "o":
            score += A[j]

    now_scores.append(score)

people_score = sorted(enumerate(now_scores), reverse=True, key=lambda x: x[1])

for i, x in enumerate(people_score):
    if i >= 2:
        break

    if i == 1:
        now_second = x[0]
    else:
        now_first = x[0]


A_with_id = list(sorted(enumerate(A), reverse=True, key=lambda x: x[1]))

for i in range(N):
    if now_scores[i] == now_scores[now_first]:
        if now_scores[now_first] == now_scores[now_second]:
            print(1)
        else:
            print(0)
        continue

    ans = 0
    need_point = now_scores[now_first] - now_scores[i]

    for num, get_point in A_with_id:
        if need_point < 0:
            print(ans)
            break

        if S[i][num] == "o":
            continue

        ans += 1
        need_point -= get_point
    else:
        print(ans)
