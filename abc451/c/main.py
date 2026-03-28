from sortedcontainers import SortedList

Q = int(input())
A = SortedList()

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        A.add(query[1])
    else:
        h = query[1]
        while len(A) > 0 and A[0] <= h:
            A.pop(0)

    print(len(A))
