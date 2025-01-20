def solve():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    now_eiyouso = [0] * M

    for _ in range(N):
        getting_eiyouso = [int(x) for x in input().split()]
        for i, eiyou in enumerate(getting_eiyouso):
            now_eiyouso[i] += eiyou

    for i in range(M):
        if A[i] > now_eiyouso[i]:
            print("No")
            return
    else:
        print("Yes")

solve()
