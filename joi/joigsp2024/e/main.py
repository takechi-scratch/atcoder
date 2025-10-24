N = int(input())
cards = [[int(x) for x in input().split()] for _ in range(N)]

ans = None

# WAポイント。全カード同じ色のケースがあることに注意！
if all(cards[i][1] == cards[0][1] for i in range(N)):
    ans = 0
elif cards[0][1] == 1 and all(x[1] == 2 for x in cards[1:]):
    ans = sum(cards[i][0] + cards[0][0] for i in range(1, N) if cards[i][0] + cards[0][0] >= 0)
else:
    max_c = -1
    max_A = -(10**18)
    for i in range(N):
        a, c = cards[i]
        if a > max_A:
            max_A = a
            max_c = c

    one_A = list(sorted((x[0] for x in cards if x[1] == max_c), reverse=True))
    two_A = list(sorted((x[0] for x in cards if x[1] != max_c), reverse=True))

    ans = 0
    for p in one_A[1:]:
        ans += max(0, two_A[0] + p)
    for p in two_A[1:]:
        ans += max(0, one_A[0] + p)
    ans += max(0, one_A[0] + two_A[0])

print(ans)
