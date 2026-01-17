# upsolve中。WAが取れない。

from atcoder.lazysegtree import LazySegTree

N, Q = [int(x) for x in input().split()]

class Dish:
    def __init__(self, reverse: int = 0, takoyaki: int = 0):
        self.reverse = reverse
        self.takoyaki = takoyaki

def mapping(f: Dish, x: Dish):
    if f.reverse > 0:
        x.takoyaki = 0
    x.reverse += f.reverse
    x.reverse %= 2

    if x.reverse == 0:
        x.takoyaki += f.takoyaki

    return x

def composition(f: Dish, g: Dish):
    if f.reverse > 0:
        return Dish(g.reverse + f.reverse, f.takoyaki)
    else:
        return Dish(g.reverse + f.reverse, g.takoyaki + f.takoyaki)


st = LazySegTree(lambda x, y: Dish((x.reverse + y.reverse) % 2, max(x.takoyaki, y.takoyaki)), Dish(0, 0), mapping, composition, Dish(0, 0), N)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        l, r, x = query[1] - 1, query[2], query[3]
        st.apply(l, r, Dish(0, x))
    elif query[0] == 2:
        l, r = query[1] - 1, query[2]
        st.apply(l, r, Dish(1, 0))
    else:
        l, r = query[1] - 1, query[2]
        print(st.prod(l, r).takoyaki)
