# 初めはNを左端に、そこから右に動かしていく

from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]

# 種類数とそれぞれの数を保持する
former_chars, latter_chars = defaultdict(int), defaultdict(int)
f_count, l_count = len(set(A)), 0

for x in A:
    former_chars[x] += 1

ans = len(former_chars)
for i in range(N - 1, 0, -1):
    # その数がいなくなったら種類-1
    former_chars[A[i]] -= 1
    if former_chars[A[i]] == 0:
        f_count -= 1

    # 初めて入ってきたら+1
    latter_chars[A[i]] += 1
    if latter_chars[A[i]] == 1:
        l_count += 1

    ans = max(f_count + l_count, ans)

print(ans)
