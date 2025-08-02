N, L, R = [int(x) for x in input().split()]
S = input()
if S[L - 1:R] == "o" * (R - L + 1):
    print("Yes")
else:
    print("No")
