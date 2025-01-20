# WA解答。
# メモリを800MBくらい使うのは厳しい…

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
MOD = 10 ** 8
mod_cnt = [0] * MOD
for i in range(N):
    ans += A[i] * 2
    mod_cnt[A[i] - 1] += 1

temp = 0
for i in range(MOD):
    if i > 0:
        mod_cnt[i] += mod_cnt[i - 1]

mod_over_cnt = 0
for i in range(N):
    mod_over_cnt += N - mod_cnt[A[i] - 1] - 1

ans -= mod_over_cnt // 2
print(ans)
