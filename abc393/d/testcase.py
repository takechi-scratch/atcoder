from random import randint
N = 50
print(N)
# print("".join([str(randint(0, 1)) for _ in range(N)]))

l = [0] * 50
for _ in range(4):
    l[randint(0, N - 1)] = 1

print("".join([str(x) for x in l]))
