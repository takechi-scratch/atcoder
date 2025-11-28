N = int(input())
A = set(int(x) for x in input().split())

for x in A:
    if x + 3 in A and x + 6 in A:
        print("Yes")
        break

else:
    print("No")
