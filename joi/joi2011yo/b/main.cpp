#include "../../cpp_macros/atcoder.h"

//----------------------------------------------

int main() {
    string target;
    ll N;
    cin >> target >> N;

    int ans = 0;
    rep(_, N){
        string test;
        cin >> test;
        rep(start, test.length()) {
            bool ok = true;
            rep(i, target.length()) {
                if (test[(start + i) % test.length()] != target[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans += 1;
                break;
            }
        }
    }
    cout << ans << endl;
}
