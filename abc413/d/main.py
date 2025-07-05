def judge(B):
    if len(B) == 0:
        return False

    for i in range(1, N - 1):
        if B[i - 1] * B[i + 1] != B[i] ** 2:
            return False

    return True

def solve(N: int, A: list[int]):
    plus = len([x for x in A if x > 0])
    if plus == N:
        pass
    elif plus == 0:
        A = [-x for x in A]
    elif N % 2 == 0 and plus * 2 == N:
        pass
    elif N % 2 == 1 and N // 2 + 1 == plus:
        pass
    elif N % 2 == 1 and N // 2 == plus:
        A = [-x for x in A]
    else:
        return False

    if all(x > 0 for x in A):
        B = list(sorted(A))
        return judge(B)
    else:
        positive = list(sorted((x for x in A if x > 0), reverse=True))
        negative = list(sorted((x for x in A if x < 0)))
        B = []
        while len(positive) > 0 or len(negative) > 0:
            if len(positive) > 0:
                B.append(positive.pop())
            if len(negative) > 0:
                B.append(negative.pop())

        B2 = []
        if N % 2 == 0:
            positive = list(sorted((x for x in A if x > 0), reverse=True))
            negative = list(sorted((x for x in A if x < 0)))
            B2 = []
            while len(positive) > 0 or len(negative) > 0:
                if len(negative) > 0:
                    B2.append(negative.pop())
                if len(positive) > 0:
                    B2.append(positive.pop())

        return judge(B) or judge(B2)



T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print("Yes" if solve(N, A) else "No")
