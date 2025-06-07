K = int(input())
A, B = [int(x) for x in input().split()]
for x in range(A, B + 1):
    if x % K == 0:
        print("OK")
        break

else:
    print("NG")
