L, R = [int(x) for x in input().split()]
ans = 0

# 再帰関数で実装
def count(now, left_ketas):
    """now: これまでに決まった文字列、left_ketas: これから決める桁数"""
    global ans

    # これから決める桁数が0の場合は、ansが範囲内か確認
    if left_ketas <= 0:
        if L <= int(now) <= R:
            ans += 1
        return

    # 現時点で生成される範囲を出しておく
    # WAポイント！f文字列のダブルクォーテーションに注意（CEになるので大丈夫ではあるが）
    generate_min, generate_max = int(now + str('0' * left_ketas)), int(now + str(int(now[0]) - 1) * left_ketas)

    # 生成される範囲が全て入っているならOK
    if L <= generate_min and generate_max <= R:
        # int(now[0]): 1桁目
        # 1桁目が5の場合は、2桁目以降は0~4の5通り（↑と等しい）
        # そのパターンが残りの桁数分
        ans += int(now[0]) ** left_ketas
        return

    # 生成される範囲が条件の端を含んでいる場合
    if generate_min <= L <= generate_max or generate_min <= R <= generate_max:
        # 次の桁を作る（21行目と同様に、0から1桁目の数まで）
        for i in range(int(now[0])):
            # 1桁進む（nowに1文字足し、left_ketasを1引く）
            count(now + str(i), left_ketas - 1)

# Lの長さからRの長さまで
# 例：10から1000までだったら、jは2~4でループ
for i in range(len(str(L)), len(str(R)) + 1):
    # はじめの桁を決定
    for j in range(1, 10):
        count(str(j), i - 1)

print(ans)
