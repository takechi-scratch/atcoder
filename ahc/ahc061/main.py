from collections import deque
import random
import time

START = time.time()
random.seed(0)

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def read_initial_input():
    N, M, T, U = [int(x) for x in input().split()]
    V = [[int(x) for x in input().split()] for _ in range(N)]
    sx, sy = [0] * M, [0] * M
    for p in range(M):
        sx[p], sy[p] = [int(x) for x in input().split()]

    owner = [[-1] * N for _ in range(N)]
    level = [[0] * N for _ in range(N)]
    px, py = list(sx), list(sy)
    for p in range(M):
        owner[sx[p]][sy[p]] = p
        level[sx[p]][sy[p]] = 1

    return N, M, T, U, V, owner, level, px, py


def get_candidates(N, M, owner, px, py, player=0):
    reachable = {(px[player], py[player])}
    queue = deque([(px[player], py[player])])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in reachable and owner[nx][ny] == player:
                reachable.add((nx, ny))
                queue.append((nx, ny))

    candidates = set(reachable)
    for x, y in reachable:
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < N and 0 <= ny < N:
                candidates.add((nx, ny))

    for p in range(M):
        if p != player:
            candidates.discard((px[p], py[p]))

    return candidates


def read_turn_result(N, M, owner, level, px, py):
    for _ in range(M):
        tx, ty = [int(x) for x in input().split()]
    for p in range(M):
        px[p], py[p] = [int(x) for x in input().split()]
    for i in range(N):
        row = [int(x) for x in input().split()]
        for j in range(N):
            owner[i][j] = row[j]
    for i in range(N):
        row = [int(x) for x in input().split()]
        for j in range(N):
            level[i][j] = row[j]


def get_random_score(
    N: int,
    M: int,
    left_T: int,
    U: int,
    V: list[list[int]],
    owner: list[list[int]],
    level: list[list[int]],
    px: list[int],
    py: list[int],
    next_move: tuple[int, int],
):
    # N = 10, 2 <= M <= 8のとき
    # 計算回数: left_T * M * N^2 = left_T * 800程度

    V = [[x for x in y] for y in V]
    owner = [[x for x in y] for y in owner]
    level = [[x for x in y] for y in level]
    px = [x for x in px]
    py = [x for x in py]

    for turn in range(left_T):
        temp_moves = []
        temp_moves_count = {}

        # O(N ** 2 + M)
        for i in range(M):
            if turn == 0 and i == 0:
                move = next_move
            else:
                move = random.choice(list(get_candidates(N, M, owner, px, py, i)))
            temp_moves.append(move)
            if move not in temp_moves_count:
                temp_moves_count[move] = 1
            else:
                temp_moves_count[move] += 1

        # O(M)
        for i, move in enumerate(temp_moves):
            nx, ny = move
            if temp_moves_count[temp_moves[i]] > 1 and owner[nx][ny] != i:
                # 駒は回収され、領土更新は行われない
                continue

            # 続けてそのまま領土更新フェーズを行う
            if owner[nx][ny] == -1:
                owner[nx][ny] = i
                level[nx][ny] = 1
            elif owner[nx][ny] == i:
                if level[nx][ny] + 1 <= U:
                    level[nx][ny] += 1
            else:
                level[nx][ny] -= 1
                if level[nx][ny] <= 0:
                    owner[nx][ny] = i
                    level[nx][ny] = 1
                else:
                    # 駒の位置更新は行わない
                    continue

            px[i], py[i] = nx, ny

    scores = [0] * M
    for x in range(N):
        for y in range(N):
            i = owner[x][y]
            if i >= 0:
                scores[i] += V[x][y] * level[x][y]

    return scores[0] / max(scores[1:])


def solve_weighted_score_greedy(
    N: int,
    M: int,
    U: int,
    V: list[list[int]],
    owner: list[list[int]],
    level: list[list[int]],
    px: list[int],
    py: list[int],
    candidates: list[tuple[int, int]],
):
    W_REDUCE, W_JACK, W_DANGER, W_SPDANGER = 0.3, 0.9, 0.4, 1.5

    v = [0.0] * len(candidates)
    for i, cd in enumerate(candidates):
        x, y = cd
        if owner[x][y] == 0 and level[x][y] >= U:
            continue
        now_v = float(V[x][y])

        if owner[x][y] > 0:
            if level[x][y] >= 2:
                now_v *= W_REDUCE ** (level[x][y] - 1)
            else:
                now_v *= W_JACK

        danger_players = set()
        for dx, dy in zip(DX, DY):
            if not (0 <= x + dx < N and 0 <= y + dy < N):
                continue
            if owner[x + dx][y + dy] > 0:
                danger_players.add(owner[x + dx][y + dy])

        for _ in danger_players:
            if owner[x][y] == 0 and level[x][y] == 1:
                now_v *= W_SPDANGER
            else:
                now_v *= W_DANGER

        v[i] = now_v

    return v


def solve_monte_carlo_method(
    N: int,
    M: int,
    calc_T: int,
    U: int,
    V: list[list[int]],
    owner: list[list[int]],
    level: list[list[int]],
    px: list[int],
    py: list[int],
    candidates: list[tuple[int, int]],
    epochs: int,
):
    score = [0.0] * len(candidates)
    for i, cd in enumerate(candidates):
        x, y = cd
        if owner[x][y] == 0 and level[x][y] >= U:
            continue

        now_score = 0.0
        for _ in range(epochs):
            now_score += get_random_score(N, M, calc_T, U, V, owner, level, px, py, (x, y))

        score[i] = now_score / epochs

    return score


def main():
    start = time.time()
    N, M, T, U, V, owner, level, px, py = read_initial_input()

    for turn in range(T):
        candidates = list(get_candidates(N, M, owner, px, py))

        if turn < 30 or 90 <= turn or time.time() - start > 1.8:
            scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
            tx, ty = candidates[scores.index(max(scores))]
        else:
            scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
            median = list(sorted(scores, reverse=True))[min(10, len(scores) - 1)]
            candidates = [x for i, x in enumerate(candidates) if scores[i] >= median]

            scores = solve_monte_carlo_method(N, M, 10, U, V, owner, level, px, py, candidates, 3)
            tx, ty = candidates[scores.index(max(scores))]

        print(tx, ty, flush=True)
        read_turn_result(N, M, owner, level, px, py)


def main2():
    N, M, T, U, V, owner, level, px, py = read_initial_input()

    for turn in range(T):
        candidates = list(get_candidates(N, M, owner, px, py))

        if turn < 20 or time.time() - START > 1.8:
            scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
            tx, ty = candidates[scores.index(max(scores))]
        else:
            scores = solve_monte_carlo_method(N, M, 1, U, V, owner, level, px, py, candidates, 5)
            median = list(sorted(scores, reverse=True))[min(3, len(scores) - 1)]
            candidates_1 = [x for i, x in enumerate(candidates) if scores[i] >= median]

            scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
            median = list(sorted(scores, reverse=True))[min(3, len(scores) - 1)]
            candidates_2 = [x for i, x in enumerate(candidates) if scores[i] >= median]

            candidates = list(set(candidates_1 + candidates_2))

            scores = solve_monte_carlo_method(N, M, min(5, T - turn - 1), U, V, owner, level, px, py, candidates, 15)
            tx, ty = candidates[scores.index(max(scores))]

        print(tx, ty, flush=True)
        read_turn_result(N, M, owner, level, px, py)


if __name__ == "__main__":
    main2()


# if 90 <= turn or time.time() - start > 1.7:
#     scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
#     tx, ty = candidates[scores.index(max(scores))]
# else:
#     scores = solve_weighted_score_greedy(N, M, U, V, owner, level, px, py, candidates)
#     median = list(sorted(scores, reverse=True))[min(5, len(scores) // 2)]
#     candidates = [x for i, x in enumerate(candidates) if scores[i] >= median]

#     scores = solve_monte_carlo_method(N, M, 10, U, V, owner, level, px, py, candidates, 2)
#     tx, ty = candidates[scores.index(max(scores))]
