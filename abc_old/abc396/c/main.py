N, M = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]

B.sort(reverse=True)
W.sort(reverse=True)

ans = 0
B_in, W_in = 0, 0
for i in range(min(N, M)):
    if B[i] <= 0:
        break
    ans += B[i]
    B_in += 1

while B_in < N or W_in < M:
    if W_in < M and W_in < B_in and W[W_in] > 0:
        ans += W[W_in]
        W_in += 1
    elif B_in < N and B[B_in] > 0:
        ans += B[B_in]
        B_in += 1
    elif W_in < M and B_in < N and B[B_in] + W[W_in] > 0:
        ans += B[B_in] + W[W_in]
        B_in += 1
        W_in += 1
    else:
        break

print(ans)
