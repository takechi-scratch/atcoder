// 解説AC。（ACLが使えるならとC++の練習）

// 初のセグ木
// 「1点更新」→「区間取得」はセグ木で高速化できる。
// 公式ドキュメント: https://github.com/atcoder/ac-library/blob/master/document_ja/segtree.md

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

vl op(vl a, vl b) {
    ll first, first_count, second, second_count;

    if (a[0] > b[0]) {
        swap(a, b);  // C++のスワップは簡単！！
    }

    if (a[0] == b[0]) {
        first = a[0];
        first_count = a[1] + b[1];
        if (a[2] == b[2]) {
            second = a[2];
            second_count = a[3] + b[3];
        } else if (a[2] > b[2]) {
            second = a[2];
            second_count = a[3];
        } else {
            second = b[2];
            second_count = b[3];
        }
    } else {
        first = b[0];
        first_count = b[1];
        if (a[0] == b[2]) {
            second = a[0];
            second_count = a[1] + b[3];
        } else if (a[0] > b[2]) {
            second = a[0];
            second_count = a[1];
        } else {
            second = b[2];
            second_count = b[3];
        }
    }

    return {first, first_count, second, second_count};
}

vl e() {
    return {-1, 0, -1, 0};
}

int main() {
    // op(vl {5, 1, -1, 0}, vl {-1, 0, -1, 0});

    ll N, Q;
    cin >> N >> Q;
    vl A(N);
    rep(i, N) {cin >> A[i];}

    segtree<vl, op, e> seg(N);
    rep(i, N) {seg.set(i, {A[i], 1, -1, 0});};

    rep(i, Q) {
        ll type;
        cin >> type;
        if (type == 1) {
            ll p, x;
            cin >> p >> x;
            seg.set(p - 1, {x, 1, -1, 0});
        } else {
            ll l, r;
            cin >> l >> r;  // 1大きい
            vl res = seg.prod(l - 1, r);
            cout << res[3] << endl;
        }
    };
}
