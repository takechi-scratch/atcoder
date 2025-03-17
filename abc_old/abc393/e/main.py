N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

max_A = max(A)
count = [0] * max_A
for x in A:
    count[x - 1] += 1

multiple_count = [0] * max_A
for i in range(1, max_A + 1):
    for j in range(i, max_A + 1, i):
        multiple_count[i - 1] += count[j - 1]

ans = [0] * max_A
for i in range(1, max_A + 1):
    if multiple_count[i - 1] < K:
        continue

    for ans_to in range(i, max_A + 1, i):
        ans[ans_to - 1] = i

for x in A:
    print(ans[x - 1])
