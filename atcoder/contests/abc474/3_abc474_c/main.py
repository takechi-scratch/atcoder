N, Q = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
query = [int(input()) for _ in range(Q)]
ans = []
appeared = set()
for x in reversed(query):
    if x in appeared:
        continue

    ans.append(x)
    appeared.add(x)

for x in reversed(P):
    if x not in appeared:
        ans.append(x)

print(*reversed(ans), sep=" ")
