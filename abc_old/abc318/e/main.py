N = int(input())
A = [int(x) for x in input().split()]

num_place = [[] for _ in range(N)]
for i, x in enumerate(A):
    num_place[x - 1].append(i)

ans = 0

# 例として1を見ているとき、
# 1 # # 1 # 1 のような中で "1, #, 1" のような選び方がいくつあるかを求める

for places in num_place:
    if len(places) <= 1:
        continue

    now_ans = 0
    cur = 0
    for j in range(len(places) - 1):
        cur += (places[j + 1] - places[j] - 1) * (j + 1)
        now_ans += cur

    ans += now_ans

print(ans)
