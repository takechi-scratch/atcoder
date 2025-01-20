S = input()
T = input()

def solve():
    if S == T:
        print("0")
        return

    for i in range(max(len(S), len(T))):
        # 長さが足りなくなったら強制的に終了。前の条件がTrueなら後ろは評価されないはず
        if i >= len(S) or i >= len(T) or S[i] != T[i]:
            print(i + 1)
            return

solve()
