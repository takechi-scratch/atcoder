N = int(input())
X = [int(x) for x in input().split()]

ans = []
for i in range(N):
    if i == 0 or i == N - 1:
        ans.append((X[-1] - X[0]) // 2)
    else:
        left_far = X[i] - X[0]
        right_far = X[-1] - X[i]
        left_near = X[i] - X[i - 1]
        right_near = X[i + 1] - X[i]

        ans.append(
            min(
                max(right_far // 2, right_near // 2 + left_far // 2),
                max(left_far // 2, left_near // 2 + right_far // 2),
            )
        )

print(*ans, sep="\n")
