#include "../../cpp_macros/atcoder.h"

//----------------------------------------------

int main() {
    ll N;
    cin >> N;
    string S, T;
    cin >> S >> T;
    ll ans = 0;
    rep(i, N) if (S[i] != T[i]) ans += 1;
    cout << ans << endl;
}
