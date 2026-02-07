from sortedcontainers import SortedList

N = int(input())
S = input()

A = [0]
for x in S:
    A.append(A[-1] + (x == "A") - (x == "B"))

SA = SortedList(A)
ans = 0
for i, x in enumerate(A[:-1]):
    ans += len(SA) - SA.bisect_right(x)
    SA.remove(x)

print(ans)
