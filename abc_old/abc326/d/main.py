# 結局は再帰で実装（条件の判定をしながら全探索するだけ）

from itertools import combinations

N = int(input())
R, C = input(), input()
ABC = "ABC"


def write_row(row: int, now_C: list[str], col_contain: list[list[str]], result: list[list[str]]):
    if row == N:
        print("Yes")
        print("\n".join(["".join(x) for x in result]))
        exit()

    for rput in combinations(range(N), 3):
        next_board = ["."] * N
        next_board[rput[0]] = R[row]
        left_index = ABC.index(R[row])
        for swap in range(1, -2, -2):
            next_C = now_C.copy()
            next_board[rput[1]] = ABC[(left_index + swap) % 3]
            next_board[rput[2]] = ABC[(left_index - swap) % 3]

            for col in range(N):
                if next_C[col] == "." and next_board[col] != ".":
                    if C[col] != next_board[col]:
                        break
                    next_C[col] = next_board[col]
            else:
                next_col_contain = [[j for j in i] for i in col_contain]
                for col in range(N):
                    if next_board[col] == ".":
                        continue

                    next_str_index = ABC.index(next_board[col])

                    if next_col_contain[col][next_str_index]:
                        break

                    next_col_contain[col][next_str_index] = True

                    if row == N - 1:
                        ok = True
                        for i in range(3):
                            if next_str_index == i:
                                continue

                            if not next_col_contain[col][next_str_index]:
                                ok = False
                                break

                        if not ok:
                            break

                else:
                    write_row(row + 1, next_C, next_col_contain, result + [next_board])
                    # return next_board, next_C

        # return None


write_row(0, ["."] * N, [[False] * 3 for _ in range(N)], [])
print("No")

