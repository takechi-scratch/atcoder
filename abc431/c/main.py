N, M, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

H.sort()
B.sort()
for x, y in zip(H[:K], B[M - K :]):
    if x > y:
        print("No")
        break

else:
    print("Yes")
