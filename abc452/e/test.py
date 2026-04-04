N = 24

x = [0] * 24
for i in range(1, 12):
    x[N % i] += 1

print(x)
