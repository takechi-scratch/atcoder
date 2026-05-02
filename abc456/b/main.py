A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

ok = 0
for i in A:
    for j in B:
        for k in C:
            if {i, j, k} == {4, 5, 6}:
                ok += 1

print(ok / 216)
