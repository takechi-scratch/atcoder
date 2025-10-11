# 愚直にやったらさすがにTLEだよね

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def tansaku(now, chosen_sum):
    chosen_sum %= M

    if now < 0:
        return int(chosen_sum % M == 0)

    return tansaku(now - 1, chosen_sum) + tansaku(now - 2, chosen_sum - A[now])


print(tansaku(N - 1, 0))
