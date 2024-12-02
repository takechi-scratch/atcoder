N, D = [int(x) for x in input().split()]
A = input()

# スタート時の空き箱と、食べた分増える空き箱を足す
print(A.count(".") + D)
