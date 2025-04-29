N = int(input())
print("Yes" if [input() for _ in range(N)].count("For") > N // 2 else "No")
