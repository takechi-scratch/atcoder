# https://atcoder.jp/contests/abc307/tasks/abc307_b
N = int(input())
S = []
for _ in range(N):
    S.append(input())

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        test = S[i] + S[j]

        for k in range(len(test) // 2 + 1):
            if test[k] != test[-1 * k - 1]:
                break
        else:
            print("Yes")
            exit()

print("No")
