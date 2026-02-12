N, K = [int(x) for x in input().split()]
things = [[int(x) for x in input().split()] for _ in range(N)]

things.sort(key=lambda x: x[0] - x[1], reverse=True)
print(sum(x[1] for x in things[:K]) + sum(x[0] for x in things[K:]))
