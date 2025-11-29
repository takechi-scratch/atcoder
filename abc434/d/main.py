# imosで集合を持つことは考えない方がいい！！！！！！！！！！！！！！！！！！！！！！！
# とりあえず、どこが覆われているかを数える→それぞれの長方形領域を+1するimos法
# 1種類が覆う領域しかいらない→長方形領域に+kすれば、どの雲が入ったかが分かる

N = int(input())
clouds = [[int(x) - 1 for x in input().split()] for _ in range(N)]
add_c = [[set()] * 2000 for _ in range(2000)]
sub_c = [[set()] * 2000 for _ in range(2000)]

for i, cloud in enumerate(clouds):
    u, d, l, r = cloud
    d += 1
    r += 1
    add_c[u][l].add(i)
    sub_c[u][r].add(i)
    sub_c[d][l].add(i)
    add_c[d][r].add(i)


cloud_sum = [[None] * 2000 for _ in range(2000)]
# 反映前のものを入れる
cloud_sum[0][0] = [set(), set()]

for x in range(1, 2000):
    for j in range(x + 1):
        i = x - j

    now = [set(), set()]
    if i > 0:
        now = cloud_sum[i - 1][j]
    if j > 0:
        before = cloud_sum[i][j - 1]
        now[0] += before[0]
        now[0]

    now = set()
    for j in range(2000):
        now |= add_c[i][j]
        now -= sub_c[i][j]

        cloud_row_sum.append(now)
