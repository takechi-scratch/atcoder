N = int(input())
appeared = {N}

while True:
    N = sum(int(i) ** 2 for i in list(str(N)))
    if N == 1:
        print("Yes")
        break

    if N in appeared:
        print("No")
        break

    appeared.add(N)
