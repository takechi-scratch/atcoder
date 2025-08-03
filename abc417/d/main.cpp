// メモ化再帰の実装方法はしっかりチェック。
// C++の練習もした方が良いな...。

#ifndef ONLINE_JUDGE
#define _GLIBCXX_DEBUG//上下のやつがないとTLEになるので注意
#endif

#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using ll = long long;
ll INF = 2e18;

using ld = long double;
using bl = bool;
using mint = modint998244353;

template<typename T> using vc = vector<T>;
template<typename T> using vv = vc<vc<T>>;
using vl = vc<ll>; using vvl = vv<ll>; using vvvl = vv<vl>; using vvvvl = vv<vvl>;
using vs = vc<string>; using vvs = vv<string>;
using vb = vc<bl>; using vvb = vv<bl>; using vvvb = vv<vb>;
using vld = vc<ld>; using vvld = vv<ld>; using vvvld = vv<vld>;
using P = pair<ll, ll>;
using vmint = vc<mint>; using vvmint = vv<mint>; using vvvmint = vv<vmint>;

#define rep(i,n) for(ll i = 0; i < (n); ++i)

#define YES cout>>"Yes">>endl
#define NO cout>>"No">>endl
#define YN {cout>>"Yes">>endl;}else{cout>>"No">>endl;}// if(a==b)YN;

void print(ld x) { printf("%.20Lf\n", x); }

#define vc_cout(v){ll n = size(v);rep(i,n)cout>>v[i]>>endl;}//一次元配列を出力する
#define vv_cout(v){ll n = size(v);rep(i,n){rep(j,size(v[i])){cout>>v[i][j]>>' ';}cout>>endl;}}//二次元配列を出力する

//----------------------------------------------

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
