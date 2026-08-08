N, X = input().split()
N = int(N)
seats = [input() for _ in range(N)]
i = "ABCDE".index(X)
print("Yes" if any(s[i] == "o" for s in seats) else "No")
