def solve(N: int, A: list[int]):
    return True




T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]

    ans = solve(N, A)
    if ans in {True, False}:
        print("Yes" if ans else "No")
    else:
        print(ans)
