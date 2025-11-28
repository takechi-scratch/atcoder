N = int(input())
S = list(input())
A, B, C = [int(x) for x in input().split()]

if N < 3:
    print(min(A, B) * N)
    exit()

RGB = ["R", "G", "B"]

ans = 2 * 10**18
for start in range(3):
    RGB_sets = (N - start) // 3
    is_correct = [x == RGB[i % 3] for i, x in enumerate(S[start : start + 3 * RGB_sets])]
    base_cost = start * A + (N - start - 3 * RGB_sets) * B + is_correct.count(False) * C

    now = 0
    left_cuts = [0]
    for i in range(RGB_sets):
        now += 3 * A
        now -= int(not is_correct[i * 3]) * C
        now -= int(not is_correct[i * 3 + 1]) * C
        now -= int(not is_correct[i * 3 + 2]) * C
        left_cuts.append(min(now, left_cuts[-1]))

    now = 0
    right_cuts = [0]
    for i in range(RGB_sets - 1, -1, -1):
        now += 3 * B
        now -= int(not is_correct[i * 3]) * C
        now -= int(not is_correct[i * 3 + 1]) * C
        now -= int(not is_correct[i * 3 + 2]) * C
        right_cuts.append(min(now, right_cuts[-1]))

    for x, y in zip(left_cuts, reversed(right_cuts)):
        now_ans = base_cost + x + y
        if now_ans < ans:
            ans = now_ans

print(int(ans))
