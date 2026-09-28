N, S, L = [int(x) for x in input().split()]
S -= 1
A = [int(x) for x in input().split()]
pos = [0]
for x in A:
    pos.append(pos[-1] + x)

ans = 1
for left in range(N - 1):
    for right in range(left + 1, N):
        if not left <= S <= right:
            continue

        l_dist = pos[S] - pos[left]
        r_dist = pos[right] - pos[S]

        if l_dist + r_dist + min(l_dist, r_dist) <= L:
            ans = max(ans, right - left + 1)

print(ans)
