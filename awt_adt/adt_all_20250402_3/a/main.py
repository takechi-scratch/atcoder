N = int(input())
T, A = 0, 0
for _ in range(N):
    x, y = [int(x) for x in input().split()]
    T += x
    A += y

if T > A:
    print("Takahashi")
elif A > T:
    print("Aoki")
else:
    print("Draw")
