N = int(input())
A = [int(x) for x in input().split()]

counter = [0] * N
for x in A:
    counter[x - 1] += 1

counter_choice_2 = [x * (x - 1) // 2 if x >= 2 else 0 for x in counter]

ans = 0
sum_c_2 = sum(counter_choice_2)
for i, x in enumerate(counter):
    ans += x * (sum_c_2 - counter_choice_2[i])

print(ans)
