S = input()
if "a" not in S:
    print(-1)
else:
    print(len(S) - list(reversed(S)).index("a"))
