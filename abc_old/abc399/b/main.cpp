#include "../../cpp_macros/atcoder.h"

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
