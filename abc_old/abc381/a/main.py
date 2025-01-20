N = int(input())
S = input()

def judge_1122(N, S):
    # 1文字だけの場合はコーナーケースとして
    if S == "/":
        print("Yes")
        return

    # 文字の長さ、間がスラッシュじゃなければアウト
    if N % 2 != 1 or S[N//2] != "/":
        print("No")
        return

    # スラッシュ前がすべて1→1の数を数えて一致するか確認
    if S[0:N//2].count("1") == N // 2 and S[N//2+1:N].count("2") == N // 2:
        print("Yes")
    else:
        print("No")

judge_1122(N, S)
