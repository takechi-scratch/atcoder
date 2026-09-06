i = 10

for a1 in range(1, i // 2 + 1):
    for a2 in range(a1, i - a1):
        a3 = i - a1 - a2
        if not (a1 <= a2 <= a3):
            continue

        print(a1, a2, a3)
