N = int(input())
W = [[int(x) for x in input().split()] for _ in range(N)]
D = [[int(x) for x in input().split()] for _ in range(N)]

import time
start_time = time.time()

from typing import Literal
from sys import stderr
import random

def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

MOVINGS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


class Answer:
    def __init__(self):
        self.score = -1
        self.steps = []

    def pick(self):
        self.steps.append(1)

    def drop(self):
        self.steps.append(2)

    def move(self, move: Literal["U", "D", "L", "R"], times: int = 1):
        if times > 0:
            self.steps.extend([move] * times)
        elif times < 0:
            self.steps.extend([{"U": "D", "D": "U", "L": "R", "R": "L"}[move]] * -times)

    def _calc_score_dev(self):
        return N ** 2 + 2 * N ** 3 - len(self.steps)

    def calc_score(self):
        self.score = self._calc_score_dev()
        return self.score

    def print(self):
        # print(self.score)
        print("\n".join(map(str, self.steps)))

def ans_init():
    ans = Answer()

    for i in range(N):
        for j in range(N):
            if W[i][j] == 0:
                continue
            ans.move("R", j)
            ans.move("D", i)
            ans.pick()

            ans.move("L", j)
            ans.move("U", i)

    return ans

def ans_random_nearests():
    ans = Answer()
    picked = [[False] * N for _ in range(N)]

    start_random = random.randrange(3)
    starts = []
    if start_random == 0:
        for ij in range(N * 2):
            for si in range(N):
                sj = ij - si
                if 0 <= sj < N:
                    starts.append((si, sj))
    elif start_random == 1:
        for i in range(N):
            for j in range(N):
                starts.append((i, j))
    else:
        for j in range(N):
            for i in range(N):
                starts.append((i, j))

    for start in starts:
        si, sj = start
        if W[si][sj] == 0 or picked[si][sj]:
            continue

        picked[si][sj] = True
        pick_boxes = [(0, 0), (si, sj)]
        sum_w = W[si][sj]
        sum_dist = si + sj
        i, j = si, sj
        before_move = "-"

        while True:
            if time.time() - start_time > 1.9:
                return

            if i == N - 1 and j == N - 1:
                break
            else:
                move = random.choices(
                    list("DRUL"),
                    weights=[(19 - i) ** 0.5, (19 - j) ** 0.5, 1 + random.random() ** 2 * 0.2, 1 + random.random() ** 2 * 0.2],
                    k=1
                )[0]
            di, dj = MOVINGS[move]
            if not (0 <= i + di < N and 0 <= j + dj < N) or {"U": "D", "D": "U", "L": "R", "R": "L"}[move] == before_move:
                continue
            i, j = i + di, j + dj

            if picked[i][j] or D[i][j] <= sum_w * sum_dist:
                continue

            # if 0.5 + (i + j) / 80 * W[i][j] / 1000 < random.random():
            #     continue

            picked[i][j] = True
            dist = abs(i - pick_boxes[-1][0]) + abs(j - pick_boxes[-1][1])
            pick_boxes.append((i, j))
            sum_w += W[i][j]
            sum_dist += dist

        ans.move("D", pick_boxes[-1][0])
        ans.move("R", pick_boxes[-1][1])
        for i in range(len(pick_boxes) - 1, 0, -1):
            ans.pick()
            ans.move("U", pick_boxes[i][0] - pick_boxes[i - 1][0])
            ans.move("L", pick_boxes[i][1] - pick_boxes[i - 1][1])

    return ans

best_ans = ans_init()
best_ans.calc_score()
update_count = 0
repeat_count = 0

while time.time() - start_time < 1.9:
    ans = ans_random_nearests()
    if ans is not None and ans.calc_score() > best_ans.score:
        best_ans = ans
        update_count += 1
        debug(f"update: {time.time() = }")
    repeat_count += 1

best_ans.print()
debug(f"{repeat_count = }")
debug(f"{update_count = }")
debug(f"{time.time() - start_time = }")
debug(f"{best_ans.score = }")
