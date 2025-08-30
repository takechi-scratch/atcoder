N = int(input())
S = input()

A_pos = [i for i, x in enumerate(S) if x == "A"]

target_1 = [2 * i for i in range(N)]
diff_1 = sum(abs(x - y) for x, y in zip(A_pos, target_1))

target_2 = [2 * i + 1 for i in range(N)]
diff_2 = sum(abs(x - y) for x, y in zip(A_pos, target_2))

print(min(diff_1, diff_2))
