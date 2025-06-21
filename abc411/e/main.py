from sortedcontainers import SortedList

MOD = 998244353

N = int(input())
DICE = [[int(x) for x in input().split()] for _ in range(N)]

all_min = 0
able_max = set()
queue = SortedList()
for i, x in enumerate(DICE):
    for y in x:
        able_max.add(y)

    for y in set(x):
        queue.add((y, i, x.count(y)))

    all_min = max(all_min, min(set(x)))

able_max = list(x for x in sorted(able_max) if x >= all_min)

bunbo_INV = pow(pow(6, N, MOD), -1, MOD)
now_ok = [0] * N

while len(queue) > 0 and queue[0][0] <= all_min:
    count = queue.pop(0)
    now_ok[count[1]] += count[2]

bunsi = 1
for x in now_ok:
    bunsi *= x
    bunsi %= MOD

ans = bunsi * all_min * bunbo_INV % MOD
before_bunsi = bunsi

for now_max in able_max[1:]:
    while len(queue) > 0 and queue[0][0] <= now_max:
        count = queue.pop(0)
        before_ok = now_ok[count[1]]
        bunsi = bunsi // before_ok * (before_ok + count[2]) % MOD

        now_ok[count[1]] += count[2]

    ans += (bunsi - before_bunsi) * now_max * bunbo_INV % MOD
    before_bunsi = bunsi

assert pow(bunsi * bunbo_INV, -1, MOD) == 1
print(ans % MOD)
