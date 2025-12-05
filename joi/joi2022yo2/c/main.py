H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]

ans = 0
for first_ci in range(H):
    for first_cj in range(W):
        if first_ci == H - 1 and first_cj == W - 1:
            continue

        ci = [-1, first_ci]
        cj = [-1, first_cj]

        target_score = 0
        for i in range(first_ci + 1):
            for j in range(first_cj + 1):
                target_score += A[i][j]

        now = 0
        ok = True
        for i in range(first_ci + 1, H):
            now += sum(A[i][: first_cj + 1])

            if now == target_score:
                ci.append(i)
                now = 0
            elif now > target_score:
                ok = False
                break

        if not ok or now > 0:
            continue

        now = 0
        for j in range(first_cj + 1, W):
            now += sum(A[x][j] for x in range(first_ci + 1))

            if now == target_score:
                cj.append(j)
                now = 0
            elif now > target_score:
                ok = False
                break

        if not ok or now > 0:
            continue

        for ci_i in range(len(ci) - 1):
            for cj_j in range(len(cj) - 1):
                now = 0
                for i in range(ci[ci_i] + 1, ci[ci_i + 1] + 1):
                    for j in range(cj[cj_j] + 1, cj[cj_j + 1] + 1):
                        now += A[i][j]

                if now != target_score:
                    ok = False
                    break

        if ok:
            ans += 1
            # print(ci, cj)

print(ans)
