N = int(input())

for i in range(10 ** 5):
    if N < i ** 2:
        print((i - 1) ** 2)
        exit()
