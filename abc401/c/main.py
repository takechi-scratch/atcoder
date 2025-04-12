N, K = [int(x) for x in input().split()]

if N < K:
    print(1)
    exit()

queue = [1] * K
out = 0
now_sum = K
for i in range(N - K):
    queue.append(now_sum)
    now_sum += now_sum
    now_sum %= 10 ** 9
    now_sum -= queue[out]
    out += 1

print(now_sum % 10 ** 9)
