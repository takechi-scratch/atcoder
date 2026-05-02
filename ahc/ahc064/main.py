# 入力からすべて0-indexed
# スコアは高ければ高いほど良い
# DepartureのiからSideのjにk台移動する

# from sys import stderr
from itertools import permutations
import random
import time

start_time = time.time()

R = int(input())
Y = [[int(x) for x in input().split()] for _ in range(R)]


class Move:
    def __init__(self, move_type: int, i: int, j: int, k: int):
        self.move_type = move_type
        self.i = i
        self.j = j
        self.k = k


def Side(i: int, j: int, k: int) -> Move:
    return Move(0, i, j, k)


def Departure(i: int, j: int, k: int) -> Move:
    return Move(1, i, j, k)


class Moves:
    def __init__(self, R: int, Y: list[list[int]]):
        self.R = R
        self.departure: list[list[int]] = [row[:] for row in Y]
        self.side: list[list[int]] = [[] for _ in range(R)]
        self.ans: list[list[Move[int, int, int, int]]] = []

    def add_move(self, moves: list[Move]) -> None:
        for move in moves:
            if move.move_type == 0:
                moving_trucks: list[int] = []
                for _ in range(move.k):
                    moving_trucks.append(self.departure[move.i].pop())

                for truck in moving_trucks:
                    self.side[move.j].append(truck)

            else:
                moving_trucks: list[int] = []
                for _ in range(move.k):
                    moving_trucks.append(self.side[move.j].pop())

                for truck in moving_trucks:
                    self.departure[move.i].append(truck)

        self.ans.append(moves)

    def compress_moves(self) -> None:
        ans_1 = self._compress_moves(0)
        ans_2 = self._compress_moves(1)
        if len(ans_1) < len(ans_2):
            self.ans = ans_1
        else:
            self.ans = ans_2

    def _compress_moves(self, compress_direction: int) -> list[list[Move]]:
        compressed_ans: list[list[Move[int, int, int, int]]] = []
        now_flatten_moves: list[Move[int, int, int, int]] = []
        for moves in self.ans:
            for move in moves:
                now_flatten_moves.append(move)

        for move in now_flatten_moves:
            if len(compressed_ans) == 0:
                compressed_ans.append([move])
                continue

            last_move = compressed_ans[-1][-1]
            if (compress_direction == 0 and last_move.i < move.i and last_move.j < move.j) or (
                compress_direction == 1 and last_move.i > move.i and last_move.j > move.j
            ):
                compressed_ans[-1].append(move)
            else:
                compressed_ans.append([move])

        return compressed_ans

    def output_ans(self, **kwargs) -> None:
        _print = lambda *args: print(*args, **kwargs)

        _print(len(self.ans))
        for moves in self.ans:
            _print(len(moves))

            for move in moves:
                _print(move.move_type, move.i, move.j, move.k)


def guchoku(dist: int = 0) -> Moves:
    moves = Moves(R, Y)

    for _ in range(R):
        if dist == 0:
            search_range = range(R)
        else:
            search_range = range(R - 1, -1, -1)

        for i in search_range:
            now_truck: int = moves.departure[i][-1]
            moves.add_move([Side(i, now_truck // R, 1)])

    for i in range(R):
        for _ in range(R):
            now_truck = moves.side[i][-1]
            moves.add_move([Departure((now_truck + i) % R, i, 1)])

        for j in range(R - 1, 0, -1):
            moves.add_move([Side((j + i) % R, i, 1)])

        moves.add_move([Departure(i, i, R - 1)])

    moves.compress_moves()

    return moves


def permutate() -> Moves:
    moves = Moves(R, Y)
    depareture_left = R * R

    while depareture_left > 0:
        move_candidates: list[list[Move]] = []
        index_candidates = list(range(R))
        random.shuffle(index_candidates)
        for i in index_candidates[:7]:
            if len(moves.departure[i]) == 0:
                continue

            now_candidate = Side(i, moves.departure[i][-1] // R, 1)
            for j in range(len(moves.departure[i]) - 2, -1, -1):
                if moves.departure[i][-1] // R != moves.departure[i][j] // R:
                    break
                else:
                    now_candidate.k += 1

            move_candidates.append([now_candidate])

        best_ordered_moves = [c[:] for c in move_candidates]
        for now_moves in permutations(move_candidates):
            now_moves = list(now_moves)

            compressed_moves: list[list[Move[int, int, int, int]]] = []
            for move in now_moves:
                if len(compressed_moves) == 0:
                    compressed_moves.append(move[:])
                    continue

                last_move = compressed_moves[-1][-1]
                if last_move.i < move[0].i and last_move.j < move[0].j:
                    compressed_moves[-1] = compressed_moves[-1] + move
                else:
                    compressed_moves.append(move[:])

            if len(compressed_moves) < len(best_ordered_moves):
                best_ordered_moves = [m[:] for m in compressed_moves]

        for now_moves in best_ordered_moves:
            moves.add_move(now_moves)
            depareture_left -= sum(move.k for move in now_moves)

    for i in range(R):
        for _ in range(R):
            now_truck = moves.side[i][-1]
            moves.add_move([Departure(now_truck % R, i, 1)])

        moves.add_move([Side(i * 2 + 1, i, 1) for i in range(R // 2)])
        moves.add_move([Side(i * 2, i, 1) for i in range(R // 2)])

        for j in range(R // 2):
            moves.add_move([Departure(i, j, 2)])

    return moves


best_moves = guchoku(dist=0)

moves = guchoku(dist=1)
if len(moves.ans) < len(best_moves.ans):
    best_moves = moves

while time.time() - start_time < 1.9:
    moves = permutate()
    if len(moves.ans) < len(best_moves.ans):
        best_moves = moves


best_moves.output_ans()
