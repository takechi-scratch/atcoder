# https://atcoder.jp/contests/abc328/tasks/abc328_d
S = input()

queue = []

for x in S:
    queue.append(x)

    while len(queue) >= 3 and queue[-3] + queue[-2] + queue[-1] == "ABC":
        [queue.pop() for _ in range(3)]

print(*queue, sep="")
