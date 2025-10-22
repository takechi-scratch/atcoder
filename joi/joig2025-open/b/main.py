N, K = [int(x) for x in input().split()]
A = [[int(x) - 1 for x in input().split()] for _ in range(N)]

ans = 0

for i in range(N - 1):
    for j in range(N - 1):
        if len({A[i][j], A[i][j + 1], A[i + 1][j], A[i + 1][j + 1]}) >= 3:
            ans += 1

colors = set()
for i in range(N):
    for j in range(N):
        colors.add(A[i][j])

strict = len(colors) == K

max_ans = 0
for ci in range(N):
    for cj in range(N):
        losts = 0

        if ci < N - 1 and cj < N - 1 and len({A[ci][cj + 1], A[ci + 1][cj], A[ci + 1][cj + 1]}) >= 2:
            losts += len({A[ci][cj], A[ci][cj + 1], A[ci + 1][cj], A[ci + 1][cj + 1]}) >= 3
            if strict:
                change1 = set(range(K)) - {A[ci][cj + 1], A[ci + 1][cj], A[ci + 1][cj + 1]}
            else:
                change1 = {-1}
        else:
            change1 = set()

        if ci < N - 1 and cj > 0 and len({A[ci][cj - 1], A[ci + 1][cj], A[ci + 1][cj - 1]}) >= 2:
            losts += len({A[ci][cj], A[ci][cj - 1], A[ci + 1][cj], A[ci + 1][cj - 1]}) >= 3
            if strict:
                change2 = set(range(K)) - {A[ci][cj - 1], A[ci + 1][cj], A[ci + 1][cj - 1]}
            else:
                change2 = {-1}
        else:
            change2 = set()

        if ci > 0 and cj < N - 1 and len({A[ci][cj + 1], A[ci - 1][cj], A[ci - 1][cj + 1]}) >= 2:
            losts += len({A[ci][cj], A[ci][cj + 1], A[ci - 1][cj], A[ci - 1][cj + 1]}) >= 3
            if strict:
                change3 = set(range(K)) - {A[ci][cj + 1], A[ci - 1][cj], A[ci - 1][cj + 1]}
            else:
                change3 = {-1}
        else:
            change3 = set()

        if ci > 0 and cj > 0 and len({A[ci][cj - 1], A[ci - 1][cj], A[ci - 1][cj - 1]}) >= 2:
            losts += len({A[ci][cj], A[ci][cj - 1], A[ci - 1][cj], A[ci - 1][cj - 1]}) >= 3
            if strict:
                change4 = set(range(K)) - {A[ci][cj - 1], A[ci - 1][cj], A[ci - 1][cj - 1]}
            else:
                change4 = {-1}
        else:
            change4 = set()

        if len(change1 & change2 & change3 & change4) > 0:
            max_ans = max(max_ans, 4 - losts)
        elif (
            len(change1 & change2 & change3) > 0
            or len(change1 & change2 & change4) > 0
            or len(change1 & change3 & change4) > 0
            or len(change2 & change3 & change4) > 0
        ):
            max_ans = max(max_ans, 3 - losts)
        elif (
            len(change1 & change2) > 0
            or len(change1 & change3) > 0
            or len(change1 & change4) > 0
            or len(change2 & change3) > 0
            or len(change2 & change4) > 0
            or len(change3 & change4) > 0
        ):
            max_ans = max(max_ans, 2 - losts)
        elif len(change1 | change2 | change3 | change4) > 0:
            max_ans = max(max_ans, 1 - losts)

print(ans + max_ans)
