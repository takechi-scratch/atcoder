from collections import Counter

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
AC = Counter(A)
all_sum = [key * value for key, value in AC.items()]
all_sum.sort()

print(sum(all_sum[: len(all_sum) - K]) if len(all_sum) > K else 0)
