from sys import exit

N, Y = [int(x) for x in input().split()]

for eiichi in range(N + 1):
    for umeko in range(N - eiichi + 1):
        shiba = N - eiichi - umeko
        if 0 <= shiba <= N and eiichi * 10000 + umeko * 5000 + shiba * 1000 == Y:
            print(eiichi, umeko, shiba)
            exit()

print("-1 -1 -1")
