N = int(input())
print(*[i if i % 3 != 0 else "Fizz" for i in range(1, N + 1)], sep="\n")
