# しゃくとり法をがんばってみた

N, M, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

# 初めに累積和をとっておくのがベスト。
b_minutes = 0
for b_index in range(M):
    b_minutes += B[b_index]

    if b_minutes > K:
        break

if b_minutes > K:
    b_minutes -= B[b_index]
    b_index -= 1


ans = b_index + 1
a_minutes = 0
# Aの読む冊数を固定して、Bを最大で読める冊数を減らしていく
for a_index in range(N):
    if a_minutes > K:
        a_index -= 1
        break

    a_minutes += A[a_index]
    while a_minutes + b_minutes > K:
        # Bをもっと減らさないといけない状況になったらアウト
        if b_index < 0:
            break

        b_minutes -= B[b_index]
        b_index -= 1


    else:
        ans = max(ans, a_index + b_index + 2)
        continue

    break

# ans = max(ans, a_index + b_index + 2)
print(ans)
