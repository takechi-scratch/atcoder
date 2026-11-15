N = int(input())
A = [int(x) for x in input().split()]

record = set([tuple(A)])

for i in range(N):
    AA = A[:]
    p = AA.pop(i)
    for j in range(i):
        AA.insert(j, p)
        record.add(tuple(AA))
        AA.pop(j)

    print(len(record))
