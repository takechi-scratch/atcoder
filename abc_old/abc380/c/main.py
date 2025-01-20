N, K = [int(x) for x in input().split()]
S = input()

start = int(S[0])
str_counts = []
bef = S[0]
count = 0
for i in range(N):
    if S[i] == bef:
        count += 1
    else:
        str_counts.append(count)
        bef = S[i]
        count = 1
str_counts.append(count)
str_counts.append(0)
str_counts.append(0)

str_counts[K * 2 - start - 2 - 1] += str_counts[K * 2 - start - 1]
str_counts[K * 2 - start + 1 - 1] += str_counts[K * 2 - start - 1 - 1]

del str_counts[K * 2 - start - 1]
del str_counts[K * 2 - start - 1 - 1]

for numbers in str_counts:
    print(str(start) * numbers, end="")
    start = 1 - start

print("")
