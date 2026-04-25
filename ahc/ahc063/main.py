from sys import stderr, exit
from collections import deque
import random
import time

start = time.time()
random.seed(42)

N, M, C = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
f = [[int(x) for x in input().split()] for _ in range(N)]

Dij = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


class Ouroboros:
    def __init__(self, N: int, M: int, C: int, d: list[int], f: list[list[int]]):
        self.N = N
        self.M = M
        self.C = C
        self.destination = [x for x in d]
        self.field = [[f[i][j] for j in range(N)] for i in range(N)]

        self.color = deque([1, 1, 1, 1, 1])
        self.pos = deque([(4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])
        self.pos_set = set(self.pos)
        self.left_feed = M - 5

        # スコアは小さい方が良い
        self.score = 10000 * (M - 5) * 2

        self.ans: list[str] = []
        self.history_new_head: list[tuple[int, int]] = []
        self.history_ate: list[bool] = []
        self.history_eaten_color: list[int] = []
        self.history_has_tail: list[bool] = []
        self.history_tail: list[tuple[int, int]] = []
        self.history_prev_score: list[int] = []
        self.history_prev_left_feed: list[int] = []
        self.history_chomped: list[bool] = []

        self.best_ans: list[str] = []
        self.best_score = self.score

    def move(self, direction: str):
        if len(self.pos) < 2 or len(self.color) < 2:
            raise ValueError("Not enough segments to move")

        head = self.pos[0]
        if direction in Dij:
            di, dj = Dij[direction]
            new_head = (head[0] + di, head[1] + dj)
        else:
            raise ValueError("Invalid direction")

        if not self.is_valid_move(direction):
            raise ValueError("Invalid move")

        i, j = new_head

        if not (0 <= i < self.N and 0 <= j < self.N):
            raise ValueError("Out of bounds")

        prev_score = self.score
        prev_left_feed = self.left_feed
        tail = None
        ate = False
        eaten_color = 0
        chomped = False

        self.pos.appendleft(new_head)

        if self.field[new_head[0]][new_head[1]] != 0:
            eaten_color = self.field[new_head[0]][new_head[1]]
            self.color.append(eaten_color)
            self.field[new_head[0]][new_head[1]] = 0
            ate = True

            if len(self.pos) - 1 < len(self.destination) and eaten_color == self.destination[len(self.pos) - 1]:
                self.score -= 10000 * 2
            else:
                self.score -= 10000

            self.left_feed -= 1
        else:
            tail = self.pos.pop()
            self.pos_set.remove(tail)

        if self.pos[0] in self.pos_set:
            chomped = True
            while self.pos[0] in self.pos_set:
                tail = self.pos.pop()
                self.pos_set.remove(tail)
                self.field[tail[0]][tail[1]] = self.color[-1]

                now_color = self.color.pop()
                if len(self.pos) < len(self.destination) and self.destination[len(self.pos)] == now_color:
                    self.score += 10000 * 2
                else:
                    self.score += 10000

                self.left_feed += 1

        self.pos_set.add(new_head)
        self.ans.append(direction)
        self.score += 1

        self.history_new_head.append(new_head)
        self.history_ate.append(ate)
        self.history_eaten_color.append(eaten_color)
        self.history_has_tail.append(tail is not None)
        self.history_tail.append(tail if tail is not None else (-1, -1))
        self.history_prev_score.append(prev_score)
        self.history_prev_left_feed.append(prev_left_feed)
        self.history_chomped.append(chomped)

        if self.score + 1 < self.best_score:
            self.best_score = self.score
            self.best_ans = self.ans[:]

    def undo(self):
        if not self.history_new_head:
            raise ValueError("No move to undo")

        if self.score < self.best_score:
            self.best_score = self.score
            self.best_ans = self.ans[:]

        chomped = self.history_chomped.pop()
        prev_left_feed = self.history_prev_left_feed.pop()
        prev_score = self.history_prev_score.pop()
        tail = self.history_tail.pop()
        has_tail = self.history_has_tail.pop()
        eaten_color = self.history_eaten_color.pop()
        ate = self.history_ate.pop()
        new_head = self.history_new_head.pop()

        if chomped:
            raise ValueError("Undo is undefined after chomp move")

        if not self.ans:
            raise ValueError("No answer history to undo")

        self.ans.pop()

        popped_head = self.pos.popleft()
        if popped_head != new_head:
            raise ValueError("State mismatch during undo")

        self.pos_set.remove(new_head)

        if ate:
            self.field[new_head[0]][new_head[1]] = eaten_color
            self.color.pop()
        else:
            if not has_tail:
                raise ValueError("State mismatch during undo")
            self.pos.append(tail)
            self.pos_set.add(tail)

        self.score = prev_score
        self.left_feed = prev_left_feed

    def output_ans(self, **kwargs):
        if self.score < self.best_score:
            print("\n".join(self.ans), **kwargs)
        else:
            print("\n".join(self.best_ans), **kwargs)

    def is_valid_move(self, direction: str) -> bool:
        if len(self.pos) < 2:
            return False

        head = self.pos[0]
        if direction in Dij:
            di, dj = Dij[direction]
            new_head = (head[0] + di, head[1] + dj)
        else:
            return False

        if new_head == self.pos[1]:
            return False

        i, j = new_head

        if not (0 <= i < self.N and 0 <= j < self.N):
            return False

        return True


def guchoku():
    best_ob = Ouroboros(N, M, C, d, f)
    for _ in range(4, N - 1):
        best_ob.move("D")

    for col in range(1, N):
        best_ob.move("R")
        if col % 2 == 1:
            for _ in range(N - 1):
                best_ob.move("U")
        else:
            for _ in range(N - 1):
                best_ob.move("D")

    return best_ob


def guchoku2():
    best_ob = Ouroboros(N, M, C, d, f)
    for _ in range(4, N - 1):
        best_ob.move("D")

    now = N - 1
    while now > 0:
        for _ in range(now):
            best_ob.move("R")

        for _ in range(now):
            best_ob.move("U")

        now -= 1

        if now == 0:
            break

        for _ in range(now):
            best_ob.move("L")

        for _ in range(now):
            best_ob.move("D")

        now -= 1

    return best_ob


def guchoku3():
    best_ob = Ouroboros(N, M, C, d, f)
    for _ in range(4, N - 1):
        best_ob.move("D")

    best_ob.move("R")

    for i in range(N):
        if i % 2 == 1:
            for _ in range(N - 2):
                best_ob.move("L")
        else:
            for _ in range(N - 2):
                best_ob.move("R")

        if i != N - 1:
            best_ob.move("U")

    return best_ob


def random_walk():
    ob = Ouroboros(N, M, C, d, f)

    c = 0
    before_weight_sum = 1
    while ob.left_feed > 0 and c < N * N * 10 and time.time() - start < 1.9:
        c += 1
        move_candidates = ["R", "L", "U", "D"]
        move_weights = [100, 100, 100, 100]
        visited = [[False] * N for _ in range(N)]
        for i, j in ob.pos:
            visited[i][j] = True

        for move_idx, move in enumerate(move_candidates):
            if not ob.is_valid_move(move):
                move_weights[move_idx] = 0
                continue

            i, j = ob.pos[0][0] + Dij[move][0], ob.pos[0][1] + Dij[move][1]

            if (i, j) in ob.pos_set:
                move_weights[move_idx] = 0
                continue

            if len(ob.pos) < len(ob.destination) and ob.destination[len(ob.pos)] == ob.field[i][j]:
                move_weights[move_idx] *= 10

            if (
                len(ob.pos) < len(ob.destination)
                and ob.field[i][j] != 0
                and ob.field[i][j] != ob.destination[len(ob.pos)]
            ):
                move_weights[move_idx] //= 100

            if visited[i][j]:
                move_weights[move_idx] //= 10
                continue

        # 変更前
        # if any(weight > 0 for weight in move_weights):
        #     # print(move_weights, file=stderr)
        #     best_move = random.choices(move_candidates, weights=move_weights)[0]
        #     ob.move(best_move)
        #     visited[ob.pos[0][0]][ob.pos[0][1]] = True
        # else:
        #     try:
        #         ob.undo()
        #     except Exception:
        #         break

        now_weight_sum = sum(move_weights)

        if now_weight_sum == 0:
            try:
                ob.undo()
            except Exception:
                break

            continue

        if max(now_weight_sum / before_weight_sum, 1) >= random.uniform(0.3, 1.1):
            # print(move_weights, file=stderr)
            best_move = random.choices(move_candidates, weights=move_weights)[0]
            ob.move(best_move)
            visited[ob.pos[0][0]][ob.pos[0][1]] = True

            before_weight_sum = now_weight_sum
        else:
            ob.undo()

    return ob


def random_walk_no_tear():
    ob = Ouroboros(N, M, C, d, f)

    c = 0
    before_weight_sum = 1
    while ob.left_feed > 0 and c < N * N * 10 and time.time() - start < 1.9:
        c += 1
        move_candidates = ["R", "L", "U", "D"]
        move_weights = [100, 100, 100, 100]
        visited = [[False] * N for _ in range(N)]
        for i, j in ob.pos:
            visited[i][j] = True

        for move_idx, move in enumerate(move_candidates):
            if not ob.is_valid_move(move):
                move_weights[move_idx] = 0
                continue

            i, j = ob.pos[0][0] + Dij[move][0], ob.pos[0][1] + Dij[move][1]

            if (i, j) in ob.pos_set:
                move_weights[move_idx] = 0
                continue

            if len(ob.pos) < len(ob.destination) and ob.destination[len(ob.pos)] == ob.field[i][j]:
                move_weights[move_idx] *= 10

            if (
                len(ob.pos) < len(ob.destination)
                and ob.field[i][j] != 0
                and ob.field[i][j] != ob.destination[len(ob.pos)]
            ):
                move_weights[move_idx] = 0
                continue

            if visited[i][j]:
                move_weights[move_idx] //= 10
                continue

        now_weight_sum = sum(move_weights)

        if now_weight_sum == 0:
            try:
                ob.undo()
            except Exception:
                break

            continue

        if max(now_weight_sum / before_weight_sum, 1) >= random.uniform(0.3, 1.1):
            # print(move_weights, file=stderr)
            best_move = random.choices(move_candidates, weights=move_weights)[0]
            ob.move(best_move)
            visited[ob.pos[0][0]][ob.pos[0][1]] = True

            before_weight_sum = now_weight_sum
        else:
            ob.undo()

    return ob


ob_guchoku_candidates = [guchoku(), guchoku2(), guchoku3()]
best_ob = min(ob_guchoku_candidates, key=lambda x: x.score)

try:
    random_best_ob: Ouroboros = random_walk()
except ValueError as e:
    print(f"Error occurred in initial random_walk: {e}", file=stderr)
    print(f"Using guchoku solution instead", file=stderr)
    random_best_ob = best_ob
random_count = 0

while time.time() - start < 1.0:
    try:
        ob = random_walk_no_tear()
    except ValueError as e:
        print(f"Error occurred: {e}", file=stderr)
        break

    print(ob.score, file=stderr)

    random_count += 1
    if ob.score < random_best_ob.score:
        random_best_ob = ob

while time.time() - start < 1.8:
    try:
        ob = random_walk()
    except ValueError as e:
        print(f"Error occurred: {e}", file=stderr)
        continue

    print(ob.score, file=stderr)

    random_count += 1
    if ob.score < random_best_ob.score:
        random_best_ob = ob

print(f"{random_best_ob.score = }", file=stderr)
random_best_ob.output_ans(file=stderr)

if random_best_ob.score < best_ob.score:
    best_ob = random_best_ob


best_ob.output_ans()
print(f"{best_ob.score = }", file=stderr)
print(f"{random_count = }", file=stderr)
