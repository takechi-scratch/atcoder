from functools import total_ordering
from sortedcontainers import SortedSet

Q, V = [int(x) for x in input().split()]


@total_ordering
class Charger:
    def __init__(self, V, T):
        self.V = V
        self.T = T

    def __eq__(self, value):
        return (self.V - self.T) == (value.V - value.T)

    def __lt__(self, other):
        return (self.V - self.T) < (other.V - other.T)

    def __hash__(self):
        return hash((self.V, self.T))


S = SortedSet()
for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        S.add(Charger(query[2], query[1]))

    else:
        if len(S) == 0:
            print(-1)
            continue

        t = query[1]
        now = S.pop()
        print(min(V, now.V + t - now.T))
