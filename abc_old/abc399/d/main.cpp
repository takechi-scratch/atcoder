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

#define YES cout<<"Yes"<<endl
#define NO cout<<"No"<<endl
#define YN {cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}// if(a==b)YN;

void print(ld x) { printf("%.20Lf\n", x); }

#define vc_cout(v){ll n = size(v);rep(i,n)cout<<v[i]<<endl;}//一次元配列を出力する
#define vv_cout(v){ll n = size(v);rep(i,n){rep(j,size(v[i])){cout<<v[i][j]<<' ';}cout<<endl;}}//二次元配列を出力する

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
