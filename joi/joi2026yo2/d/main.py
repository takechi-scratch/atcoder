from bisect import bisect_left

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()


A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)


def calc_sum(c: int, d: int, coupon_count: int) -> int:
    discount_value = d * coupon_count

    if discount_value >= A_sum[-1]:
        things_sum = 0
    else:
        zero_things = bisect_left(A, discount_value)
        things_sum = A_sum[-1] - A_sum[zero_things] - discount_value * (N - zero_things)

    return things_sum + c * coupon_count


ans = []
for _ in range(Q):
    c, d = [int(x) for x in input().split()]

    low, high = 0, A[-1] // d + 10
    while high - low > 2:
        mid1 = (low * 2 + high) // 3
        mid2 = (low + high * 2) // 3

        if calc_sum(c, d, mid1) <= calc_sum(c, d, mid2):
            high = mid2
        else:
            low = mid1

        if high < low:
            raise RuntimeError()

    ans.append(min(calc_sum(c, d, low), calc_sum(c, d, low + 1), calc_sum(c, d, high)))

print("\n".join(str(x) for x in ans))
