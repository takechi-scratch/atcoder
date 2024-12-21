N = int(input())
H = [int(x) for x in input().split()]
# もともとansを1にしておけば2WAにはならなかった。初期値にも注意。
ans = 0

# WAポイント！コーナーケースに注意。
if N == 1:
    print(1)
    exit()

# 発想の転換大事！！
# 「数字を見て位置を決める」ではなく「位置を見て数字を決める」考え方
for distance in range(1, N - 1):
    # スタートの位置が変わるので注意。
    for start in range(distance):
        now_tall = -1
        now_ans = 0
        for i in range(start, N, distance):
            ans = max(ans, now_ans)
            if H[i] == now_tall:
                now_ans += 1
            else:
                now_tall = H[i]
                now_ans = 1
            ans = max(ans, now_ans)

print(ans)
