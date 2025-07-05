from itertools import permutations

def solve(N: int, A: list[int]):
    for B in permutations(A, N):
        for i in range(1, N - 1):
            if B[i - 1] * B[i + 1] != B[i] ** 2:
                break
        else:
            return True

    return False


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print("Yes" if solve(N, A) else "No")
