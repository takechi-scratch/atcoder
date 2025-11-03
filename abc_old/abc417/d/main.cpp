// メモ化再帰の実装方法はしっかりチェック。
// C++の練習もした方が良いな...。

#include "../../cpp_macros/atcoder.h"

unordered_map<ll, ll> memo;
int N;
vvl gifts;


ll solve(int finished, int now_point) {
    ll key = finished * 100000LL + now_point;
    if (memo.count(key)) return memo[key];
    if (finished >= N) {
        memo[key] = now_point;
        return now_point;
    };
    if (now_point <= gifts[finished][0]) {
        now_point += gifts[finished][1];
    } else {
        now_point -= gifts[finished][2];
        now_point = max(now_point, 0);
    }

    ll result = solve(finished + 1, now_point);
    memo[key] = result;
    return result;
}

int main() {
    cin >> N;
    int p, a, b;
    rep(_, N) {
        cin >> p >> a >> b;
        gifts.push_back({p, a, b});
    }

    vl down_points_sum = {0};
    rep(i, N) {
        down_points_sum.push_back(down_points_sum[down_points_sum.size() - 1] + gifts[i][2]);
    }

    // rep(i, down_points_sum.size()) {
    //     cout << down_points_sum[i] << endl;
    // }

    int Q;
    cin >> Q;
    rep(_, Q) {
        int X;
        cin >> X;
        if (X <= 1000) {
            cout << solve(0, X) << endl;
            continue;
        }

        auto it = upper_bound(down_points_sum.begin(), down_points_sum.end(), X - 1000);
        int downs = it - down_points_sum.begin();

        if (downs >= down_points_sum.size()) {
            cout << X - down_points_sum[down_points_sum.size() - 1] << endl;
            continue;
        }

        int now_point = X - down_points_sum[downs];
        cout << solve(downs, now_point) << endl;
    }
}
