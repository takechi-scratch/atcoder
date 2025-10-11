N = int(input())


def f(num):
    return sum(int(x) for x in str(num))


A = [1]

for _ in range(N):
    num = 0
    for x in A:
        num += f(x)
    A.append(num)

print(A[-1])
