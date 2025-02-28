# かなりの重実装。
# 満足度が1番大きいものが、2番目に大きいものと同じになるまで乗る（2番目以降も繰り返す）
# こうすることで、↑の各ステップの回数と、満足度の総和をO(1)で出せる！！

# 確認用テストケースあり（下へ）

def ap_sum(start, end):
    # 等差数列の和（テンプレコード）
    assert start <= end
    return (start + end) * (end - start + 1) // 2

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.append(0)  # 足しても影響なし
A.sort()

ans = 0
now_eq = 0  # ←WAポイント！N=1のときはforの部分でnow_eqが定義されない。
for now_eq in range(1, N):
    if A[N - now_eq] == A[N - now_eq + 1]:
        continue

    ans_plus = ap_sum(A[N - now_eq] + 1, A[N - now_eq + 1]) * now_eq
    steps = (A[N - now_eq + 1] - A[N - now_eq]) * now_eq

    if steps > K:
        break

    ans += ans_plus
    K -= steps
else:
    # ここでエラーになる
    now_eq += 1

# 端数処理
if K >= now_eq:
    after = A[N - now_eq + 1] - K // now_eq
    if after > 0:
        ans += ap_sum(A[N - now_eq + 1] - K // now_eq + 1, A[N - now_eq + 1]) * now_eq
        ans += (A[N - now_eq + 1] - K // now_eq) * (K % now_eq)
    else:
        ans += ap_sum(1, A[N - now_eq + 1]) * now_eq

else:
    ans += A[N - now_eq + 1] * K

print(ans)

# 追加で試したテストケース（良ければご参考までに）
"""
3 100
1 1 1
"""

"""
3 5
1 2 3
"""

"""
1 1
5
"""
