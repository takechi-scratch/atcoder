N = int(input())
A = [int(x) for x in input().split()]

numbers = {}
for x in A:
    if x not in numbers:
        numbers[x] = 0
    numbers[x] += 1

for x in sorted(numbers.keys(), reverse=True):
    if numbers[x] > 1:
        continue

    for i in range(N):
        if A[i] == x:
            print(i + 1)
            exit()

print(-1)
