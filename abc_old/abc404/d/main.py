N, M = [int(x) for x in input().split()]
raw_c = [int(x) for x in input().split()]
zoos = [[] for _ in range(2 * N)]
for i in range(M):
    watchable_zoos = [int(x) - 1 for x in input().split()][1:]
    for j in watchable_zoos:
        zoos[2 * j].append(i)
        zoos[2 * j + 1].append(i)

C = []
for x in raw_c:
    C.append(x)
    C.append(x)

ans = 10 ** 18
for i in range(2 ** (2 * N)):
    visit_raw = bin(i)[2:]
    visit = ["0"] * (2 * N - len(visit_raw)) + list(visit_raw)

    for i in range(0, 2 * N, 2):
        if visit[i] == "1" and visit[i + 1] == "0":
            break

    else:
        animals = [0] * M
        temp_ans = 0
        for i in range(2 * N):
            if visit[i] == "1":
                temp_ans += C[i]
                for j in zoos[i]:
                    animals[j] += 1

        for i in animals:
            if i < 2:
                break
        else:
            ans = min(ans, temp_ans)

print(ans)
