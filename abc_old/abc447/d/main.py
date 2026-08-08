from collections import deque

S = input()

Aq = deque()
Bq = deque()
ans = 0

for i, x in enumerate(S):
    if x == "A":
        Aq.append(i)
    elif x == "B" and len(Aq) > 0:
        Aq.popleft()
        Bq.append(i)
    elif x == "C" and len(Bq) > 0:
        Bq.popleft()
        ans += 1

print(ans)
