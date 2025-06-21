// Original Python Code:
/*
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
    while len(queue) > 0 and queue[0][0] == now_max:
        count = queue.pop(0)
        before_ok = now_ok[count[1]]
        bunsi = bunsi // before_ok * (before_ok + count[2]) % MOD

        now_ok[count[1]] += count[2]

    ans += (bunsi - before_bunsi) * now_max * bunbo_INV % MOD
    before_bunsi = bunsi

assert pow(bunsi * bunbo_INV, -1, MOD) == 1
print(ans % MOD)
*/

#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

// Modular exponentiation
long long mod_pow(long long a, long long b, long long mod) {
    long long res = 1;
    while(b > 0) {
        if(b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

// Modular inverse
long long mod_inv(long long a, long long mod) {
    return mod_pow(a, mod - 2, mod); // Fermat's little theorem
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> DICE(N, vector<int>(6));
    set<int> able_max;
    multiset<tuple<int, int, int>> queue;
    int all_min = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 6; ++j) {
            cin >> DICE[i][j];
            able_max.insert(DICE[i][j]);
        }

        set<int> unique;
        for (int j = 0; j < 6; ++j) {
            unique.insert(DICE[i][j]);
        }

        for (int val : unique) {
            int count = count_if(DICE[i].begin(), DICE[i].end(), [&](int x){ return x == val; });
            queue.insert({val, i, count});
        }

        int local_min = *min_element(unique.begin(), unique.end());
        all_min = max(all_min, local_min);
    }

    vector<int> able_max_vec;
    for (int val : able_max) {
        if (val >= all_min) able_max_vec.push_back(val);
    }

    long long bunbo = mod_pow(6, N, MOD);
    long long bunbo_INV = mod_inv(bunbo, MOD);

    vector<int> now_ok(N, 0);

    while (!queue.empty() && get<0>(*queue.begin()) <= all_min) {
        auto count = *queue.begin();
        queue.erase(queue.begin());
        now_ok[get<1>(count)] += get<2>(count);
    }

    long long bunsi = 1;
    for (int x : now_ok) {
        bunsi = bunsi * x % MOD;
    }

    long long ans = bunsi * all_min % MOD * bunbo_INV % MOD;
    long long before_bunsi = bunsi;

    for (size_t idx = 1; idx < able_max_vec.size(); ++idx) {
        int now_max = able_max_vec[idx];
        while (!queue.empty() && get<0>(*queue.begin()) == now_max) {
            auto count = *queue.begin();
            queue.erase(queue.begin());

            int i = get<1>(count);
            int cnt = get<2>(count);
            int before_ok = now_ok[i];

            bunsi = bunsi * mod_inv(before_ok, MOD) % MOD;
            bunsi = bunsi * (before_ok + cnt) % MOD;
            now_ok[i] += cnt;
        }

        ans = (ans + (bunsi - before_bunsi + MOD) % MOD * now_max % MOD * bunbo_INV % MOD) % MOD;
        before_bunsi = bunsi;
    }

    assert(mod_inv(bunsi * bunbo_INV % MOD, MOD) == 1);
    cout << ans % MOD << endl;

    return 0;
}
