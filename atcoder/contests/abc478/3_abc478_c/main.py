from collections import defaultdict

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
target = list(sorted(A))
ok = [A[i] == target[i] for i in range(N)]
ok_count = ok[K:].count(True)

diff = defaultdict(int)
diff_count = 0

for x in A[:K]:
    diff[x] += 1

for x in target[:K]:
    diff[x] -= 1

for item in diff.values():
    if item != 0:
        diff_count += 1


def replace(i: int, dist: int):
    global diff_count

    if diff[i] != 0:
        diff_count -= 1

    diff[i] += dist

    if diff[i] != 0:
        diff_count += 1


if diff_count == 0 and ok_count == N - K:
    print("Yes")
else:
    for i in range(N - K):
        replace(A[i], -1)
        replace(A[i + K], 1)

        replace(target[i], 1)
        replace(target[i + K], -1)

        ok_count += ok[i]
        ok_count -= ok[i + K]

        if diff_count == 0 and ok_count == N - K:
            print("Yes")
            break

    else:
        print("No")
