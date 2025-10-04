#include "../../cpp_macros/atcoder.h"

//----------------------------------------------


int main() {
    ll N, M;
    cin >> N >> M;
    vl A(N), B(M);
    rep(i, N){
        cin >> A[i];
    }
    rep(i, M){
        cin >> B[i];
    }

    ll ans = 0;
    rep(i, N){
        rep(j, M){
            ans += max(A[i], B[j]) * (A[i] + B[j]);
        }
    }

    cout << ans << endl;
}
