N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
while N > 0 and A[-1] == B[-1]:
    A.pop()
    B.pop()
    N -= 1

A.reverse()
B.reverse()

while N > 0 and A[-1] == B[-1]:
    A.pop()
    B.pop()
    N -= 1

if N == 0:
    print("Yes")
else:
    A_1 = A[1:] + [A[0]]
    A_2 = [A[-1]] + A[:-1]
    if A_1 == B or A_2 == B:
        print("Yes")
    else:
        print("No")
