#ifndef ONLINE_JUDGE
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
ll INF = 2e18;

using ld = long double;
using bl = bool;

template<typename T> using vc = vector<T>;
template<typename T> using vv = vc<vc<T>>;
using vl = vc<ll>; using vvl = vv<ll>; using vvvl = vv<vl>; using vvvvl = vv<vvl>;
using vs = vc<string>; using vvs = vv<string>;
using vb = vc<bl>; using vvb = vv<bl>; using vvvb = vv<vb>;
using vld = vc<ld>; using vvld = vv<ld>; using vvvld = vv<vld>;
using P = pair<ll, ll>;

#define rep(i,n) for(ll i = 0; i < (n); ++i)

#define YES cout<<"Yes"<<endl
#define NO cout<<"No"<<endl
#define YN {cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}// if(a==b)YN;

void print(ld x) { printf("%.20Lf\n", x); }

#define vc_cout(v){ll n = size(v);rep(i,n)cout<<v[i]<<endl;}//一次元配列を出力する
#define vv_cout(v){ll n = size(v);rep(i,n){rep(j,size(v[i])){cout<<v[i][j]<<' ';}cout<<endl;}}//二次元配列を出力する

int main() {
    ll N, M;
    cin >> N >> M;
    vvl bunnies(N);
    rep(i, N) {
        ll x, y;
        cin >> x >> y;
        bunnies[i] = {x, y};
    };
    vl T(M);
    vl T_counts(N);
    rep(i, M) {
        ll t;
        cin >> t;
        T[i] = t;
        T_counts[t - 1] += 1;
    };

    vc<P> pos_add(N);
    rep(i, N) {
        pos_add[i] = make_pair(bunnies[i][0] + bunnies[i][1], i);
    };
    vc<P> pos_sub(N);
    rep(i, N) {
        pos_sub[i] = make_pair(bunnies[i][1] - bunnies[i][0], i);
    };

    sort(pos_add.begin(), pos_add.end());
    sort(pos_sub.begin(), pos_sub.end());

    vl add_imos(N);
    vl sub_imos(N);

    rep(i, N) {
        ll x = T_counts[i];
        if (x == 0) continue;

        auto root_add = bunnies[i][0] + bunnies[i][1];
        auto root_sub = bunnies[i][1] - bunnies[i][0];
        auto now_pos_add = upper_bound(pos_add.begin(), pos_add.end(), make_pair(root_add, INF));
        auto now_pos_add2 = lower_bound(pos_add.begin(), pos_add.end(), make_pair(root_add, -INF));
        if (pos_add.end() - now_pos_add > 0) {
            add_imos[now_pos_add - pos_add.begin()] += x * 2;
        }
        add_imos[0] -= x * 2;
        add_imos[now_pos_add2 - pos_add.begin()] += x * 2;

        auto now_pos_sub = upper_bound(pos_sub.begin(), pos_sub.end(), make_pair(root_sub, INF));
        auto now_pos_sub2 = lower_bound(pos_sub.begin(), pos_sub.end(), make_pair(root_sub, -INF));
        if (pos_sub.end() - now_pos_sub > 0) {
            sub_imos[now_pos_sub - pos_sub.begin()] += x * 2;
        }
        sub_imos[0] -= x * 2;
        sub_imos[now_pos_sub2 - pos_sub.begin()] += x * 2;

    };

    ll now_add = 0;
    ll now_sub = 0;
    vl A(N), B(N);

    rep(i, N) {
        now_add += add_imos[i];
        now_sub += sub_imos[i];
        A[pos_add[i].second] = pos_add[i].first + now_add;
        B[pos_sub[i].second] = pos_sub[i].first + now_sub;
    }

    rep(i, N) {
        cout << (A[i] - B[i]) / 2 << " " << (A[i] + B[i]) / 2 << "\n";
    };

    return 0;
}
