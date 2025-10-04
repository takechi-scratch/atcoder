#include "../../cpp_macros/atcoder.h"

//----------------------------------------------

void solve() {
    ll N;
    cin >> N;
    vl A(2 * N);
    rep(i, 2 * N) cin >> A[i];

    vvl positions(N);
    rep(i, 2 * N) {
        positions[A[i] - 1].push_back(i);
    }

    ll ans = 0;
    vl di1 = {1, 1, -1, -1};
    vl di2 = {1, -1, 1, -1};
    rep(i, N) {
        ll first = positions[i][0], second = positions[i][1];
        if (first + 1 >= second) continue;

        rep(j, 4) {
            if (0 <= first + di1[j] && first + di1[j] < 2 * N && 0 <= second + di2[j] && second + di2[j] < 2 * N) {
                if (first + di1[j] + 1 >= second + di2[j]) continue;
                if (A[first + di1[j]] == A[second + di2[j]]) ans += 1;
            }
        }
    }

    cout << ans / 2 << endl;
}

int main() {
    ll T;
    cin >> T;
    rep(_, T) solve();
}
