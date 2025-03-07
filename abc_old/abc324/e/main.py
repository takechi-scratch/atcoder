# 問題文をよく読むこと！！
# 「組み合わせた時の文字の種類数」ではなく、「iとjの選び方」
# つまり、重複・複数回の選択が許される

from bisect import bisect_left

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

# 「接頭辞として何文字使えるか」と「接尾辞として何文字使えるか」
prefix_score = []
suffix_score = []

for s in S:
    ps = 0
    for i, x in enumerate(s):
        if T[ps] == x:
            ps += 1
            if ps == len(T):
                break

    prefix_score.append((ps, s))

    ss = 0
    for i, x in enumerate(reversed(s)):
        if T[-1 - ss] == x:
            ss += 1
            if ss == len(T):
                break

    suffix_score.append((ss, s))

suffix_score.sort()
S = [x[1] for x in suffix_score]
suffix_score = [x[0] for x in suffix_score]

ans = 0
# 接頭辞と接尾辞で長さ以上になればOK。二分探索で高速化
for ps in prefix_score:
    ans += N - bisect_left(suffix_score, len(T) - ps[0])

print(ans)

# 11分実装完了
