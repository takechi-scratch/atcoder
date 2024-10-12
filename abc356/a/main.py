N, L, R = [int(x) for x in input().split()]

ans = list(range(1, N + 1))
ans = ans[:L - 1] + list(reversed(ans[L-1:R])) + ans[R:]

print(" ".join([str(x) for x in ans]))
