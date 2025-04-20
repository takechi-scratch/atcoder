Q = int(input())
queue = []
# 何人入ったかをメモ
in_count = 0

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        queue.append(query[1])
    else:
        print(queue[in_count])
        in_count += 1
