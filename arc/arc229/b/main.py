def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    if not all(A[i] >= A[i + 1] for i in range(N - 1)):
        print("-1")
        return

    ans = 0
    for i in range(N - 1, -1, -1):
        if A[i] == 0:
            continue

        turns = A[i]
        ans += 1
        for j in range(i - 1, -1, -1):
            min_delete = 2 ** (i - j) * turns
            max_delete = (2 ** (i - j + 1) - 1) * turns
            if A[j] < min_delete:
                print("-1")
                return

            A[j] = max(0, A[j] - max_delete)

    print(ans)
    return


T = int(input())
for _ in range(T):
    solve()
