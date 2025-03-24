from bisect import bisect_left

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

needs_position: dict[int, list] = {}
for x in B:
    needs_position[x] = []

B_set = set(B)

for i, x in enumerate(A):
    if x not in B_set:
        continue

    needs_position[x].append(i)

left_keep = []
cur = -1
for x in B:
    pos = bisect_left(needs_position[x], cur)
    if pos >= len(needs_position[x]):
        print("No")
        exit()

    choose = needs_position[x][pos]
    left_keep.append(choose)
    cur = choose + 1

cur = 10 ** 18
for i, x in enumerate(reversed(B)):
    pos = bisect_left(needs_position[x], cur)
    if pos <= 0:
        print("No")
        exit()

    choose = needs_position[x][pos - 1]
    if choose != left_keep[M - i - 1]:
        print("Yes")
        break

    cur = choose

else:
    print("No")
