# 結局スコアの計算が面倒でできてない

class TimeKeeper:
    def __init__(self, limit):
        from time import time
        self.now = time
        self.start_time = time()

        self.limit = limit

    def isOver(self):
        return self.now() - self.start_time > self.limit

    def reset(self):
        self.start_time = self.now()


N, M, K, T = [int(x) for x in input().split()]
homes, works = [], []
for i in range(M):
    hi, hj, wi, wj = [int(x) for x in input().split()]
    homes.append((hi, hj))
    works.append((wi, wj))


class Solver:
    def __init__(self, N: int, M: int, K: int, T: int, homes: list[tuple[int, int]], works: list[tuple[int, int]]):
        self.N, self.M, self.K, self.T = N, M, K, T
        self.homes, self.works = homes.copy(), works.copy()
        self.ans, self.score = [], K

    def get_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def main(self):
        from random import randint
        N, M, K, T = self.N, self.M, self.K, self.T
        homes, works = self.homes, self.works

        # built = [[False] * N for _ in range(N)]
        ans, score = self.ans, self.score

        while True:
            connect_people = randint(1, M) - 1
            if self.get_distance(homes[connect_people], works[connect_people]) > T - len(ans) - 2:
                continue

            if self.get_distance(homes[connect_people], works[connect_people]) * 100 + 10000 > K:
                continue

            break

        hi, hj, wi, wj = homes[connect_people][0], homes[connect_people][1], works[connect_people][0], works[connect_people][1]
        if hj > wj:
            hi, hj, wi, wj = wi, wj, hi, hj

        ans.append((0, hi, hj))
        ans.append((0, wi, wj))

        if hi < wi:
            ans.extend([(2, i, hj) for i in range(hi + 1, wi)])
            ans.append((5, wi, hj))
            ans.extend([(1, wi, j) for j in range(hj + 1, wj)])
        else:
            ans.extend([(2, i, hj) for i in range(hi - 1, wi, -1)])
            ans.append((6, wi, hj))
            ans.extend([(1, wi, j) for j in range(hj + 1, wj)])

        return ans, score


time_keeper = TimeKeeper(2.7)
ans, score = [(-1)] * T, K

now_ans, now_score = Solver(N, M, K, T, homes, works).main()
if now_score >= score:
    if len(now_ans) < T:
        now_ans.extend([tuple([-1])] * (T - len(now_ans)))
    ans, score = now_ans, now_score

'''
while not time_keeper.isOver():
    now_ans, now_score = Solver(N, M, K, T, homes, works).main()
    if now_score >= score:
        if len(now_ans) < T:
            now_ans.extend([tuple([-1])] * (T - len(now_ans)))
        ans, score = now_ans, now_score
'''

print("\n".join([" ".join([str(y) for y in x]) for x in ans]))
print("# score:", score)
