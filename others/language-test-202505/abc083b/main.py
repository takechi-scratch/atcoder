N, A, B = [int(x) for x in input().split()]

ans = 0
for x in range(1, N + 1):
    digits_sum = sum(int(y) for y in str(x))
    if A <= digits_sum <= B:
        ans += x

print(ans)
