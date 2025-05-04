# またもやWA解答

def solve(H: int, W: int, S: str):
    right_count, down_count = 0, 0
    ans = 0

    all_right = (0, 0)
    all_down = (0, 0)
    for i, x in enumerate(S):
        if x == "D":
            down_count += 1
            all_right = (all_right[0] + 1, all_right[1])
            all_down = (all_down[0] + 1, all_down[1])
        elif x == "R":
            right_count += 1
            all_right = (all_right[0], all_right[1] + 1)
            all_down = (all_down[0], all_down[1] + 1)
        else:
            if right_count < W - 1:
                right_count += 1
                all_right = (all_right[0], all_right[1] + 1)
            else:
                all_right = (all_right[0] + 1, all_right[1])

            if down_count < H - 1:
                down_count += 1
                all_down = (all_down[0] + 1, all_down[1])
            else:
                all_down = (all_down[0], all_down[1] + 1)

        ans += all_right[1] - all_down[1] + 1

    return ans


T = int(input())
for _ in range(T):
    H, W = [int(x) for x in input().split()]
    S = input()
    print(solve(H, W, S))
