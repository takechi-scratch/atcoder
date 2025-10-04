#include "../../cpp_macros/atcoder.h"

//----------------------------------------------


int main() {
    ll N, M;
    cin >> N >> M;
    vl place(N), dice(M);

    rep(i, N){cin >> place[i];}
    rep(i, M){cin >> dice[i];}

    ll now = 1;
    rep(i, M){
        now += dice[i];
        if (now >= N){
            cout << i + 1 << endl;
            break;
        }
        now += place[now - 1];
        if (now >= N){
            cout << i + 1 << endl;
            break;
        }
    }
}
