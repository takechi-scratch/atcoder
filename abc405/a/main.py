R, X = [int(x) for x in input().split()]
if X == 1:
    print("Yes" if 1600 <= R <= 2999 else "No")
else:
    print("Yes" if 1200 <= R <= 2399 else "No")
