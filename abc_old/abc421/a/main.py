N = int(input())
S = [input() for _ in range(N)]

X, Y = input().split()
print("Yes" if S[int(X) - 1] == Y else "No")
