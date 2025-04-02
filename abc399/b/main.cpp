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

int main() {
    ll N;
    cin >> N;
    vl p(N);
    rep(i, N) cin >> p[i];
    vc<P> scores(N);
    rep(i, N) scores[i] = make_pair(p[i], i);

    sort(scores.rbegin(), scores.rend());
    ll now_score = 1000;
    ll now_rank = 0;
    vl ans(N);
    rep(i, N) {
        ll s, ind;
        tie(s, ind) = scores[i];
        if (s != now_score) {
            now_score = s;
            now_rank = i;
        }
        ans[ind] = now_rank + 1;
    }

    vc_cout(ans);
}
