from sortedcontainers import SortedList

Q = int(input())
A = SortedList([])

for _ in range(Q):
  query = [int(x) for x in input().split()]

  if query[0] == 1:
    A.add(query[1])

  elif query[0] == 2:
    x, k = query[1], query[2]
    right = A.bisect_right(x)
    if right < k:
      print(-1)
      continue

    print(A[right - k])

  elif query[0] == 3:
    x, k = query[1], query[2]
    left = A.bisect_left(x)
    if left > len(A) - k:
      print(-1)
      continue

    print(A[left + k - 1])
