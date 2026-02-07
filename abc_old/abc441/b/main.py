N, M = [int(x) for x in input().split()]
S = set(input())
T = set(input())
Q = int(input())

for _ in range(Q):
    text = input()
    for x in text:
        if x not in S:
            print("Aoki")
            break
        elif x not in T:
            print("Takahashi")
            break
    else:
        print("Unknown")
