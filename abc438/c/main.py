N = int(input())
A = [int(x) for x in input().split()]
B = []

for add_x in A:
    B.append(add_x)
    while len(B) >= 4:
        if B[-1] == B[-2] == B[-3] == B[-4]:
            for _ in range(4):
                B.pop()
        else:
            break

print(len(B))
