#include "../../cpp_macros/atcoder.h"

//----------------------------------------------

int main() {
    ll N, M;
    cin >> N >> M;
    dsu unionfind(N);
    ll ans = 0;
    rep(_, M) {
        ll u, v;
        cin >> u >> v;
        u -= 1, v -= 1;
        if (unionfind.same(u, v)) {
            ans += 1;
            continue;
        }
        unionfind.merge(u, v);
    }
    cout << ans << endl;
}
