N = int(input())
choose = [[] for _ in range(37)]
for i in range(N):
    C = int(input())
    A = [int(x) for x in input().split()]
    for x in A:
        choose[x].append((C, i))

X = int(input())

choose[X].sort(key=lambda a: a[0])
if len(choose[X]) == 0:
    print(0)
    print()
    exit()

ok = choose[X][0][0]
ans = []
for a in choose[X]:
    if a[0] != ok:
        break
    ans.append(a[1] + 1)

print(len(ans))
print(*ans)
