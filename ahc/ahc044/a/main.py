import time

def duration():
    return time.time() - start

N, L = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

start = time.time()
import random
import sys

def score(ans):
    dates = [0] * N
    today_clean = 0
    for i in range(L):
        dates[today_clean] += 1
        today_clean = ans[today_clean][1 - dates[today_clean] % 2]

    score = 10 ** 6
    for i, x in enumerate(dates):
        score -= abs(T[i] - x)

    return score

def sequence():
    return [[(i + 1) % N] * 2 for i in range(N)]

def random_geometric_assignment():
    assignments = [x / L * N * 2 for x in T]
    next_person = []
    for i, x in enumerate(assignments):
        next_person += [i] * int(x)

    while len(next_person) > 2 * N:
        next_person.pop()

    while len(next_person) < 2 * N:
        next_person.append(random.randrange(N))

    random.shuffle(next_person)

    return [[next_person[2 * x], next_person[2 * x + 1]] for x in range(N)]

def random_including_self(half):
    now_ans = []
    for i in range(N):
        if T[i] > half:
            fixed = i
        else:
            fixed = random.randrange(N)
            while fixed == i:
                fixed = random.randrange(N)

        random_other = random.randrange(N)
        while random_other == i:
            random_other = random.randrange(N)
        if random.randint(0, 1):
            now_ans.append((random_other, fixed))
        else:
            now_ans.append((fixed, random_other))

    return now_ans

def turns_assignments(more_2: set, more_1: set, less_1: set, less_2: set):
    assignments = []
    for i, x in enumerate(T):
        if x in more_2:
            assignments.extend([i] * 4)
        elif x in more_1:
            assignments.extend([i] * 3)
        elif x in less_1:
            assignments.extend([i] * 1)
        elif x not in less_2 and x > 0:
            assignments.extend([i] * 2)

    return assignments

def random_turns_decide(threshold_1, threshold_2, limit):
    global ans
    global max_score
    global method

    more_2 = set(sorted_T[0 - threshold_1:])
    more_1 = set(sorted_T[0 - threshold_2:0 - threshold_1])
    less_1 = set(sorted_T[threshold_1:threshold_2])
    less_2 = set(sorted_T[:threshold_1])
    assignments = turns_assignments(more_2, more_1, less_1, less_2)

    while duration() < limit:
        random.shuffle(assignments)
        now_ans = [[assignments[2 * x], assignments[2 * x + 1]] for x in range(N)]
        now_score = score(now_ans)

        # print("\n".join([f"{x[0]} {x[1]}" for x in now_ans]))
        # print(now_score, file=sys.stderr)
        if now_score > max_score:
            ans = now_ans
            method = f"random_turns_decide({threshold_1}, {threshold_2}, {limit})"
            max_score = now_score

ans = sequence()
method = "sequence"
max_score = score(ans)

while duration() < 0.3:
    now_ans = random_geometric_assignment()
    now_score = score(now_ans)
    if now_score > max_score:
        ans = now_ans
        method = "random_geometric_assignment"
        max_score = now_score

sorted_T = sorted(T)
while duration() < 0.4:
    now_ans = random_including_self(sorted_T[- N // 5])
    now_score = score(now_ans)
    if now_score > max_score:
        ans = now_ans
        method = "random_including_self"
        max_score = now_score

# print(f"{duration()=}", file=sys.stderr)

random_turns_decide(3, 40, 0.7)
random_turns_decide(5, 35, 1.2)
random_turns_decide(3, 35, 1.8)

print("\n".join([f"{x[0]} {x[1]}" for x in ans]))
print(f"{score(ans)=}", file=sys.stderr)
print(f"{method=}", file=sys.stderr)
