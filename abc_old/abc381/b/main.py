S = input()

def judge_1122(S):
    # 奇数文字数ならアウト
    if len(S) % 2 != 0:
        return False

    for i in range(len(S)):
        # 各文字に対して現れる回数をチェック
        if S.count(S[i]) not in [0, 2]:
            return False

        # 偶数文字目の場合は、1文字前と同じかチェック
        if i % 2 == 1 and S[i] != S[i-1]:
            return False

    else:
        return True

print("Yes" if judge_1122(S) else "No")
