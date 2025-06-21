import time
start = time.time()

def duration():
    return time.time() - start

from sys import stderr
from itertools import combinations_with_replacement
import random
import heapq

N, K, H, T, D = [int(x) for x in input().split()]

PAINT_ADD = 1
PAINT_SUBMIT = 2
PAINT_THROW = 3
TOGGLE_PARTITION = 4

class Color:
    def __init__(self, r: float = 0.0, g: float = 0.0, b: float = 0.0, tuple_color: tuple = None):
        if tuple_color is not None:
            if not isinstance(tuple_color, tuple) or len(tuple_color) != 3:
                raise ValueError("tuple_color must be a tuple of three elements")
            r, g, b = tuple_color

        self.r = r
        self.g = g
        self.b = b

    def __add__(self,other):
        if not isinstance(other, Color):
            raise TypeError("Unsupported operand type(s) for +: 'Color' and '{}'".format(type(other).__name__))

        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self,other):
        if not isinstance(other, Color):
            raise TypeError("Unsupported operand type(s) for -: 'Color' and '{}'".format(type(other).__name__))

        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self,other):
        if isinstance(other, (int, float)):
            return Color(self.r * other, self.g * other, self.b * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Color' and '{}'".format(type(other).__name__))

    def __truediv__(self,other):
        if isinstance(other, (int, float)):
            return Color(self.r / other, self.g / other, self.b / other)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Color' and '{}'".format(type(other).__name__))

    def __eq__(self, value):
        if not isinstance(value, Color):
            raise TypeError("Unsupported operand type(s) for ==: 'Color' and '{}'".format(type(value).__name__))
        return (self.r, self.g, self.b) == (value.r, value.g, value.b)

    def __hash__(self):
        return hash((self.r, self.g, self.b))

def _action(func):
    def wrapper(self, *args, **kwargs):
        self.action_count += 1
        if self.action_count > T:
            raise RuntimeError("Action count exceeded limit T")
        result = func(self, *args, **kwargs)
        return result
    return wrapper

class Answer:
    def __init__(self, separate_col: list[list[int]] = None, separate_row: list[list[int]] = None):
        if separate_col is not None:
            self.separate_col = separate_col
        else:
            self.separate_col = [[1] * (N - 1) for _ in range(N)]

        if separate_row is not None:
            self.separate_row = separate_row
        else:
            self.separate_row = [[1] * N for _ in range(N - 1)]

        self.actions: list[list[int]] = []
        self.action_count = 0
        self.added_count = 0
        self.submit_count = 0
        self.submitted: list[Color] = []

        self.score = -1

        # 盤面状態の初期化
        self.N = N
        self.K = K
        self.H = H
        self.D = D

    def separate_4block(self):
        self.separate_col = [[0, 1] * (N // 2 - 1) + [0] for _ in range(N)]
        self.separate_row = [[i % 2] * N for i in range(N - 1)]

    @_action
    def add(self, x: int, y: int, color_num: int):
        self.actions.append([PAINT_ADD, x, y, color_num])
        self.added_count += 1

    @_action
    def submit(self, x: int, y: int, color: Color):
        self.actions.append([PAINT_SUBMIT, x, y])
        self.submit_count += 1
        self.submitted.append(color)

    @_action
    def throw(self, x: int, y: int):
        self.actions.append([PAINT_THROW, x, y])

    @_action
    def toggle_partition(self, x1: int, y1: int, x2: int, y2: int):
        self.actions.append([TOGGLE_PARTITION, x1, y1, x2, y2])

    def build_ans_from_mixdata(self, mixed_colors, mixed_colors_data_raw, best_colors):
        mixed_colors_data = []
        for data in mixed_colors_data_raw:
            mixed_colors_data.append([data[0].copy(), data[1].copy(), 0])

        for i, data in enumerate(best_colors):
            color_type, mix_num, mono_num = data
            if color_type == 0:
                self.add(0, 0, mono_num)
                self.submit(0, 0, own[mono_num])
            else:
                mix_data: tuple[list[int], set[int], int] = mixed_colors_data[mix_num]
                x, y = (mix_num + 1) // (N // 2) * 2, (mix_num + 1) % (N // 2) * 2

                if mix_data[2] % 4 == 0:
                    for k in mix_data[0]:
                        self.add(x, y, k)

                mix_data[1].discard(i)
                self.submit(x, y, mixed_colors[mix_num])

                mix_data[2] += 1

    def calc_score(self):
        # コスト
        V = self.added_count
        E = 0.0
        for i in range(min(self.H, len(self.submitted))):
            E += color_distance(target[i], self.submitted[i])
        abs_score = 1 + self.D * (V - self.submit_count) + round(1e4 * E)

        self.score = abs_score
        return abs_score

    def print(self):
        for x in self.separate_col:
            print(*x)
        for x in self.separate_row:
            print(*x)
        for action in self.actions:
            print(*action)

        print("Score:", self.calc_score(), file=stderr)
        if not self.submit_count == self.H:
            print("Warning: Not all target colors submitted", file=stderr)

def color_mix(*colors: tuple[Color]) -> Color:
    if not colors:
        raise ValueError("At least one color must be provided")

    r_sum = sum(color.r for color in colors)
    g_sum = sum(color.g for color in colors)
    b_sum = sum(color.b for color in colors)

    return Color(r_sum / len(colors), g_sum / len(colors), b_sum / len(colors))

def color_distance(color1: Color, color2: Color) -> float:
    return ((color1.r - color2.r) ** 2 +
            (color1.g - color2.g) ** 2 +
            (color1.b - color2.b) ** 2) ** 0.5

def find_closest_color(target_color: Color, own_colors: list[Color]) -> tuple[int, Color]:
    closest_color = None
    min_distance = 10 ** 18
    min_index = -1

    for i, color in enumerate(own_colors):
        distance = color_distance(target_color, color)

        if distance < min_distance:
            min_distance = distance
            closest_color = color
            min_index = i

    return min_index, closest_color


own = []
for _ in range(K):
    own.append(Color(tuple_color=tuple(float(x) for x in input().split())))

target = []
for _ in range(H):
    target.append(Color(tuple_color=tuple(float(x) for x in input().split())))

mixed_colors = []
mixed_colors_data: list[list[int, int, set, tuple[int, int]]] = []
for i in range(K):
    for j in range(i + 1, K):
        mixed_color = (own[i] + own[j]) / 2
        mixed_colors.append(mixed_color)
        mixed_colors_data.append([i, j, set(), (-1, -1)])

def ans_closest_pick():
    ans = Answer([[0] * (N - 1) for _ in range(N)], [[0] * N for _ in range(N - 1)])
    mono_best_info = []

    for i in range(H):
        closest_color_num, closest_color = find_closest_color(target[i], own)
        mono_best_info.append((0, -1, closest_color_num))
        ans.add(0, 0, closest_color_num)
        ans.submit(0, 0, closest_color)

    return ans, mono_best_info

def ans_one_two_pick():
    ans = Answer()
    ans.separate_4block()

    best_colors = []
    favorite_count = [0] * K
    for i in range(H):
        mono_i, mono_closest = find_closest_color(target[i], own)
        two_i, two_closest = find_closest_color(target[i], mixed_colors)

        if color_distance(mono_closest, target[i]) < color_distance(two_closest, target[i]):
            best_colors.append((0, -1, mono_i))
        else:
            best_colors.append((1, two_i, mono_i))
            mixed_colors_data[two_i][2].add(i)
            favorite_count[mixed_colors_data[two_i][0]] += 1
            favorite_count[mixed_colors_data[two_i][1]] += 1

    free_space = set()
    for i in range(N):
        for j in range(N // 2):
            if i == 0 and j == 0:
                continue

            free_space.add((i, j * 2))

    for i, data in enumerate(best_colors):
        color_type, two_num, mono_num = data
        if color_type == 0 or len(free_space) == 0:
            ans.add(0, 0, mono_num)
            ans.submit(0, 0, own[mono_num])
        else:
            mix_data: list[int, int, set, tuple[int, int]] = mixed_colors_data[two_num]

            if mix_data[3] == (-1, -1):
                place = free_space.pop()
                ans.add(place[0], place[1], mix_data[0])
                ans.add(place[0], place[1], mix_data[1])

                mix_data[3] = place
                mix_data[2].discard(i)
                if len(mix_data[2]) == 0:
                    ans.submit(place[0], place[1], mixed_colors[two_num])
                    ans.throw(place[0], place[1])
                    free_space.add(place)
                else:
                    ans.toggle_partition(place[0], place[1], place[0], place[1] + 1)
                    ans.submit(place[0], place[1] + 1, mixed_colors[two_num])

            else:
                place = mix_data[3]
                ans.submit(place[0], place[1], mixed_colors[two_num])
                ans.toggle_partition(place[0], place[1], place[0], place[1] + 1)
                free_space.add(place)

                mix_data[3] = (-1, -1)
                mix_data[2].discard(i)

    return ans, favorite_count

def ans_random_four_colors(favorite_count: list[int] = None, mono_best_info: list[tuple[int, int, int]] = None):
    if mono_best_info is None:
        mono_best_info = ans_closest_pick()[1]

    ans = Answer([[0, 1] * (N // 2 - 1) + [0] for _ in range(N)], [[i % 2] * N for i in range(N - 1)])
    mixed_colors: list[Color] = []
    mixed_colors_data: list[list[list[int], set[int], int]] = []
    mixed_colors_set: set[Color] = set()

    pallet_capacity = (N // 2) ** 2 - 1
    priority_pallets = pallet_capacity * random.randint(5, 30) // 100

    # 実際使う色を100色ランダムで決める（4つ混ぜる）
    while len(mixed_colors) < pallet_capacity:
        if favorite_count is not None and len(mixed_colors) < priority_pallets:
            pick_colors = random.choices(range(K), k=2, weights=favorite_count)
            pick_colors.extend([random.randrange(K) for _ in range(2)])
            pass
        else:
            pick_colors = [random.randrange(K) for _ in range(4)]

        if pick_colors[0] == pick_colors[1] == pick_colors[2] == pick_colors[3]:
            continue

        mixed_color = color_mix(*(own[i] for i in pick_colors))
        if mixed_color in mixed_colors_set:
            continue

        mixed_colors.append(mixed_color)
        mixed_colors_data.append([pick_colors, set(), 0])

    # 単色or4色混色で、より近い方を選択
    best_colors = []
    for i in range(H):
        mono_i = mono_best_info[i][2]
        mix_i, mix_closest = find_closest_color(target[i], mixed_colors)

        if color_distance(own[mono_i], target[i]) <= color_distance(mix_closest, target[i]):
            best_colors.append((0, -1, mono_i))
        else:
            best_colors.append((1, mix_i, mono_i))
            mixed_colors_data[mix_i][1].add(i)

    # 1あまりは単色にしちゃう -> 5%程度改善
    for mix_color, data in zip(mixed_colors, mixed_colors_data):
        if len(data[1]) % 4 != 1:
            continue

        odd, odd_score_diff = -1, 10 ** 18
        for x in data[1]:
            score = color_distance(target[x], own[best_colors[x][2]]) - color_distance(target[x], mix_color)
            if score < odd_score_diff:
                odd = x
                odd_score_diff = score

        data[1].discard(odd)
        best_colors[odd] = (0, -1, best_colors[odd][2])

    ans.build_ans_from_mixdata(mixed_colors, mixed_colors_data, best_colors)

    return ans, [mixed_colors, mixed_colors_data, best_colors]

def modify_color_change(mixed_colors: list[Color], mixed_colors_data: list[list[list[int], set[int], int]], best_colors):
    change = random.choice(range(len(mixed_colors)))


    after_color_sources = [x for x in mixed_colors_data[change][0]]
    after_color_sources.pop(random.randrange(4))
    after_color_sources.append(random.randrange(K))
    after_color = color_mix(*[own[x] for x in after_color_sources])

    before_diff = 0
    after_diff = 0
    i = 0
    for x in mixed_colors_data[change][1]:
        if i > 50:
            break

        before_diff += color_distance(target[x], mixed_colors[change])
        after_diff += color_distance(target[x], after_color)

        i += 1

    if after_diff < before_diff:
        mixed_colors[change] = after_color
        mixed_colors_data[change][0] = after_color_sources
        # print("Changed", file=stderr)

    return mixed_colors, mixed_colors_data, best_colors

def ans_search_perfect_colors(colors_per_block = 100):
    ans = Answer()
    ans.separate_4block()

    perfect_mixed_colors: list[tuple[Color, tuple[int, int, int, int]]] = []

    for x in combinations_with_replacement(range(K), 4):
        perfect_mixed_colors.append((color_mix(*[own[i] for i in x]), tuple(x)))

    for q in range((H - 1) // colors_per_block + 1):
        now_colors = target[q * colors_per_block: (q + 1) * colors_per_block]
        belonging_groups = [-1] * len(now_colors)
        groups: list[list[list[int], Color, tuple[int, int]]] = []
        for i in range(len(now_colors)):
            if belonging_groups[i] != -1:
                continue

            group_num = len(groups)
            now_group_colors = [i]
            belonging_groups[i] = group_num

            now_color = target[q * colors_per_block + i]

            queue = []
            heapq.heapify(queue)
            for j in range(i + 1, len(now_colors)):
                if belonging_groups[j] == -1:
                    error = int(color_distance(now_color, target[q * colors_per_block + j]) * 10000)
                    heapq.heappush(queue, (error, j))

            while len(now_group_colors) < 4 and len(queue) > 0:
                _, j = heapq.heappop(queue)
                now_group_colors.append(j)
                belonging_groups[j] = group_num

            groups.append([now_group_colors, color_mix(*[target[q * colors_per_block + j] for j in now_group_colors]), (-1, -1)])

        group_use_color_nums: list[int] = []
        for _, goal_color, _ in groups:
            goal_dist = 10 ** 18
            goal_i = -1
            for i in range(len(perfect_mixed_colors)):
                now_dist = color_distance(goal_color, perfect_mixed_colors[i][0])
                if now_dist < goal_dist:
                    goal_dist = now_dist
                    goal_i = i

            group_use_color_nums.append(goal_i)

        free_space = set()
        for i in range(N // 2):
            for j in range(N // 2):
                free_space.add((i * 2, j * 2))

        for i, x in enumerate(belonging_groups):
            group: list[list[int], Color, tuple[int, int]] = groups[x]
            mix_data = perfect_mixed_colors[group_use_color_nums[x]]
            group[0].remove(i)

            if group[2] == (-1, -1):
                place = free_space.pop()
                for j in range(4):
                    ans.add(place[0], place[1], mix_data[1][j])

                group[2] = place
                ans.submit(place[0], place[1], mix_data[0])

            else:
                place = group[2]
                ans.submit(place[0], place[1], mix_data[0])
                if len(group[0]) == 0:
                    free_space.add(place)
                    group[2] = (-1, -1)

    return ans


greedy_ans, mono_best_info = ans_closest_pick()
new_ans, favorite_count = ans_one_two_pick()
if new_ans.calc_score() < greedy_ans.calc_score():
    greedy_ans = new_ans


best_cpb = -1
for cpb in [100, 300, 325, 350, 375, 400, 425, 450]:
    try:
        new_ans = ans_search_perfect_colors(cpb)
        if new_ans.calc_score() < greedy_ans.score:
            greedy_ans = new_ans
            best_cpb = cpb
    except:
        print(f"failed reserve free space cpb: {cpb}", file=stderr)

print(f"{best_cpb = }, {greedy_ans.score = }", file=stderr)



random_ans, _ = ans_closest_pick()
random_ans.calc_score()

i = 0
best_mixdata = None
while duration() < 2.3:
    try:
        res = ans_random_four_colors(favorite_count, mono_best_info)
        if res[0].calc_score() < random_ans.score:
            random_ans = res[0]
            best_mixdata = res[1]

        i += 1
    except Exception as e:
        print("error", e, file=stderr)

random_score = random_ans.calc_score()
print(f"executed random_solve {i} times", file=stderr)

if best_mixdata is not None:
    i = 0
    while duration() < 2.7:
        best_mixdata = modify_color_change(*best_mixdata)
        i += 1

    random_ans = Answer()
    random_ans.separate_4block()
    random_ans.build_ans_from_mixdata(*best_mixdata)
    print(f"modified {i} times", file=stderr)
    print(f"score ratio: {random_ans.calc_score() / random_score * 100 :.3f}%", file=stderr)

if greedy_ans.score < random_ans.score:
    print(f"+ won greedy method! {greedy_ans.score / random_ans.score = }", file=stderr)
    greedy_ans.print()
else:
    print(f"- won random method! {random_ans.score / greedy_ans.score = }", file=stderr)
    random_ans.print()
