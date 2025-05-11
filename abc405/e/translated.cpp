/* ChatGPTによる翻訳（工夫しなくても通った）

import sys
sys.setrecursionlimit(10**9)

from functools import lru_cache

MOD = 998244353

A, B, C, D = [int(x) for x in input().split()]
N = A + B + C + D

factor = [1]
for i in range(1, A + B + C + D):
    factor.append(factor[-1] * i % MOD)

def mod_factorical(n: int, MOD: int = 998244353):
    return factor[n]

@lru_cache(maxsize=None)
def mod_comb(n: int, k: int, MOD: int = 998244353):
    ans = mod_factorical(n, MOD) * pow(mod_factorical(k, MOD), -1, MOD) % MOD
    ans = ans * pow(mod_factorical(n - k, MOD), -1, MOD) % MOD
    return ans

ans = 0

for A_end in range(A, A + B + 1):
    first_B = A_end - A
    second_B = B - first_B
    first_area = mod_comb(A_end - 1, first_B)

    second_third = mod_factorical(second_B + C + D)
    second_third *= pow(mod_factorical(second_B) * mod_factorical(C) % MOD * mod_factorical(D) % MOD * mod_comb(second_B + D, D) % MOD, -1, MOD)

    ans += first_area * second_third
    ans %= MOD

ans %= MOD
print(ans)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 998244353;

int A, B, C, D;
vector<long long> factor;

long long mod_pow(long long x, long long n, int mod) {
    long long res = 1;
    x %= mod;
    while (n > 0) {
        if (n % 2) res = res * x % mod;
        x = x * x % mod;
        n /= 2;
    }
    return res;
}

long long mod_factorial(int n) {
    return factor[n];
}

long long mod_comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    long long num = mod_factorial(n);
    long long denom = mod_factorial(k) * mod_factorial(n - k) % MOD;
    return num * mod_pow(denom, MOD - 2, MOD) % MOD;
}

int main() {
    cin >> A >> B >> C >> D;
    int N = A + B + C + D;

    factor.resize(N + 1);
    factor[0] = 1;
    for (int i = 1; i <= N; ++i) {
        factor[i] = factor[i - 1] * i % MOD;
    }

    long long ans = 0;
    for (int A_end = A; A_end <= A + B; ++A_end) {
        int first_B = A_end - A;
        int second_B = B - first_B;
        long long first_area = mod_comb(A_end - 1, first_B);

        long long second_third = mod_factorial(second_B + C + D);
        long long denom = mod_factorial(second_B) * mod_factorial(C) % MOD * mod_factorial(D) % MOD * mod_comb(second_B + D, D) % MOD;
        second_third = second_third * mod_pow(denom, MOD - 2, MOD) % MOD;

        ans = (ans + first_area * second_third % MOD) % MOD;
    }

    cout << ans << endl;
    return 0;
}
