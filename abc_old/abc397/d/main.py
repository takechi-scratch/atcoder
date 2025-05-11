from math import ceil
N = int(input())


for diff in range(1, ceil(N ** (1 / 3))):
    # Nはa-bの倍数になっているはずなので、先にチェック
    if N % diff != 0:
        continue

    # 二分探索でxの値を求める
    more, less = 1, 10 ** 18
    while less - more > 1:
        mid = (more + less) // 2
        result = mid ** 3 - (mid - diff) ** 3
        if result == N:
            print(mid, mid - diff)
            exit()
        elif result > N:
            less = mid
        else:
            more = mid

print(-1)
