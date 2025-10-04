// 解説AC。（ACLが使えるならとC++の練習）

// 初のセグ木
// 「1点更新」→「区間取得」はセグ木で高速化できる。
// 公式ドキュメント: https://github.com/atcoder/ac-library/blob/master/document_ja/segtree.md

#include "../../cpp_macros/atcoder.h"

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
