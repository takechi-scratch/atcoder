Q = int(input())
stack = [0] * 100

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        stack.append(query[1])
    else:
        print(stack.pop())
