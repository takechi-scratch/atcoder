fib = [int(x) for x in input().split()]

for i in range(2, 10):
    now = int("".join(reversed(str(fib[i - 1] + fib[i - 2]))))
    fib.append(now)

print(fib[-1])
