N, R = [int(x) for x in input().split()]

for i in range(N):
    d, a = [int(x) for x in input().split()]
    if d == 1 and 1600 <= R <= 2799:
        R += a
    elif d == 2 and 1200 <= R <= 2399:
        R += a

print(R)
