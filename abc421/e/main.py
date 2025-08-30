# なんか違う

def calc_probability(p):
    return 1 - (1 - p) ** 3

A = [int(x) for x in input().split()]

ans = 0
for x in set(A):
    now_ans = calc_probability(A.count(x) / 6) * 5 * x
    ans = max(now_ans, ans)

print(ans)
