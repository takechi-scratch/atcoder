# WAとかREとか。まだまだ考察が必要。

from collections import defaultdict

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

cake_brands = defaultdict(list)

for i, x in enumerate(A):
    cake_brands[x].append(i)

for key in cake_brands.keys():
    cake_brands[key].sort(key=lambda i: B[i])

teas = list(zip(D, C))
teas.sort()
left_cakes = set(range(N))

alone_cake_brand = set(B) - set(D)
alone_cakes = []
for key in alone_cake_brand:
    alone_cakes.extend(cake_brands[key])
alone_cakes.sort(key=lambda i: B[i])

ans = 0
for tea_deli, tea_brand in reversed(teas):
    if len(cake_brands[tea_brand]) == 0:
        cake_i = alone_cakes.pop()
        ans += B[cake_i]
        continue

    if len(alone_cakes) == 0 or B[cake_brands[tea_brand][-1]] + tea_deli >= B[alone_cakes[-1]]:
        cake_i = cake_brands[tea_brand].pop()
        ans += B[cake_i] + tea_deli
        left_cakes.remove(cake_i)
    else:
        cake_i = alone_cakes.pop()
        ans += B[cake_i]

print(ans)
