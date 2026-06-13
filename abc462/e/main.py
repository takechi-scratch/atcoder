def solve(A: int, B: int, X: int, Y: int):
    if A > B:
        A, B = B, A
        X, Y = Y, X

    need_x = abs(X)
    need_y = abs(Y)

    zigzag_turns = min(need_x, need_y)
    ans = zigzag_turns * A * 2
    need_x -= zigzag_turns
    need_y -= zigzag_turns

    add_ans_1 = 0
    if need_x > 0:
        add_ans_1 += (need_x + 1) // 2 * A
        add_ans_1 += need_x // 2 * (A * 3)
    else:
        add_ans_1 += (need_y + 1) // 2 * (A * 3)
        add_ans_1 += need_y // 2 * A

    add_ans_2 = 0
    if need_x > need_y:
        add_ans_2 += (need_x + 1) // 2 * A
        add_ans_2 += need_x // 2 * B
    else:
        add_ans_2 += (need_y + 1) // 2 * B
        add_ans_2 += need_y // 2 * A

    return ans + min(add_ans_1, add_ans_2)


T = int(input())
for _ in range(T):
    A, B, X, Y = [int(x) for x in input().split()]
    print(solve(A, B, X, Y))
