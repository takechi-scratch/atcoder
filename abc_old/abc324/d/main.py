N = int(input())
S = input()

S_max = int("".join(sorted(S, reverse=True)))

squares = []
for x in range(10 ** 8):
    if x ** 2 > S_max:
        break
    value = str(x ** 2)
    squares.append([int(x) for x in list(value)])

available = [0] * 10
for x in S:
    available[int(x)] += 1

ans = 0
for goal in squares:
    counter = [0] * 10
    if N - len(goal) > available[0]:
        continue

    counter[0] += N - len(goal)

    for x in goal:
        counter[x] += 1
        if counter[x] > available[x]:
            break

    else:
        ans += 1

print(ans)

