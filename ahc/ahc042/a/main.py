import time
# import sys
import random

def isTimeOver():
    return time.time() - start > 1.8

def score(onis, fukus, steps):
    if onis == 0 and fukus == 2 * N:
        return 8 * N ** 2 - steps
    else:
        return 4 * N ** 2 - (N - fukus + onis)

def UP(di):
    return "L" if di == "row" else "U"

def DOWN(di):
    return "R" if di == "row" else "D"

def generate_check(C, is_row, i):
    if is_row:
        return C[i]
    else:
        return [C[j][i] for j in range(N)]

# ----ここから----

N = int(input())
C = []
for _ in range(N):
    C.append(list(input()))

start = time.time()

ans = []
max_score = -1

sousa = [("row", i) for i in range(N)] + [("col", i) for i in range(N)]
def rantaku2(C: list[list[str]]):
    ans = []
    now_onis = 2 * N

    random.shuffle(sousa)

    for di, i in sousa:
        check = generate_check(C, di == "row", i)

        if "x" not in check:
            continue

        if "o" in check:
            nec_up = 0
            for j in range(N):
                if check[j] == "x":
                    if di == "row":
                        C[i][j] = "."
                    else:
                        C[j][i] = "."
                    nec_up = j + 1
                    now_onis -= 1

                elif check[j] == "o":
                    break

            nec_down = 0
            for j in range(N - 1, -1, -1):
                if check[j] == "x":
                    if di == "row":
                        C[i][j] = "."
                    else:
                        C[j][i] = "."
                    nec_down = N - j
                    now_onis -= 1

                elif check[j] == "o":
                    break

        else:
            onis = [i for i, x in enumerate(check) if x == "x"]
            if max(onis) + 1 < N - min(onis):
                nec_up = max(onis) + 1
                nec_down = 0
            else:
                nec_up = 0
                nec_down = N - min(onis)

        if nec_up < nec_down:
            ans.extend([(UP(di), i)] * nec_up)
            ans.extend([(DOWN(di), i)] * (nec_up + nec_down))

            if "x" not in check:
                after_fukus = [i + nec_down for i, x in enumerate(check) if x == "o"]
                for fuku in after_fukus:
                    if "x" in generate_check(C, 1 - (di == "row"), fuku):
                        break
                else:
                    if di == "row":
                        for j in range(N - nec_down):
                            C[i][j + nec_down] = C[i][j]
                        for j in range(nec_down):
                            C[i][j] = "."
                    else:
                        for j in range(N - nec_down):
                            C[j + nec_down][i] = C[j][i]
                        for j in range(nec_down):
                            C[j][i] = "."

                    continue

            ans.extend([(UP(di), i)] * nec_down)

        else:
            ans.extend([(DOWN(di), i)] * nec_down)
            ans.extend([(UP(di), i)] * (nec_up + nec_down))

            if "x" not in check:
                after_fukus = [i - nec_up for i, x in enumerate(check) if x == "o"]
                for fuku in after_fukus:
                    if "x" in generate_check(C, 1 - (di == "row"), fuku):
                        break
                else:
                    if di == "row":
                        for j in range(N - nec_up - 1, -1, -1):
                            C[i][j] = C[i][j + nec_up]
                        for j in range(nec_up):
                            C[i][N - 1 - j] = "."
                    else:
                        for j in range(N - nec_up - 1, -1, -1):
                            C[j][i] = C[j + nec_up][i]
                        for j in range(nec_up):
                            C[N - 1 - j][i] = "."

                    continue

            ans.extend([(DOWN(di), i)] * nec_up)

    return ans, now_onis

while not isTimeOver():
    now_ans, onis = rantaku2([x[:] for x in C])
    now_score = score(onis, 2 * N, len(now_ans))
    if now_score > max_score:
        max_score = now_score
        ans = now_ans

if len(ans) <= 4 * N ** 2:
    print(*[f"{x[0]} {x[1]}" for x in ans], sep="\n")

# print("--------------------", file=sys.stderr)
# print("time:", time.time() - start, file=sys.stderr)
# print("score:", max_score, file=sys.stderr)
# print("steps:", len(ans), file=sys.stderr)
