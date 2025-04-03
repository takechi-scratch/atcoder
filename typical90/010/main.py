N = int(input())
scores = [[] for _ in range(2)]
for i in range(N):
    c, p = [int(x) for x in input().split()]
    c -= 1
    scores[c].append(p)
    scores[1 - c].append(0)

sum_1, sum_2 = [0], [0]
for i in range(N):
    sum_1.append(sum_1[-1] + scores[0][i])
    sum_2.append(sum_2[-1] + scores[1][i])

Q = int(input())

for _ in range(Q):
    l, r = [int(x) for x in input().split()]

    print(sum_1[r] - sum_1[l - 1], sum_2[r] - sum_2[l - 1])
