N = int(input())
customers = [[int(x) for x in input().split()] for _ in range(N)]

M = int(input())
plans = [[int(x) for x in input().split()] for _ in range(M)]

max_t = max(*[x[1] for x in customers + plans]) + 100

start_sum = [0] * (max_t + 1)
for x, _, c in customers:
    start_sum[x] += c

for i in range(1, max_t + 1):
    start_sum[i] += start_sum[i - 1]

end_sum = [0] * (max_t + 1)
for _, x, c in customers:
    end_sum[x + 1] += c

for i in range(1, max_t + 1):
    end_sum[i] += end_sum[i - 1]

ans = []
sum_incomes = sum(x[2] for x in customers)
for s, t in plans:
    ans.append(sum_incomes - end_sum[s] - (sum_incomes - start_sum[t]))

print(*ans, sep="\n")
