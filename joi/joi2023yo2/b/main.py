N = int(input())
classes = [[int(x) for x in input().split()] for _ in range(4)]

people = []
for i, kumi in enumerate(classes):
    for x in kumi:
        people.append((x, i))

people.sort()

leaders = [-1, -1, -1, -1]
ans = 10**18
for p in people:
    leaders[p[1]] = p[0]
    if not any(x == -1 for x in leaders):
        ans = min(ans, max(leaders) - min(leaders))

print(ans)
