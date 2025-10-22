#include "../../../cpp_macros/atcoder.h"

//----------------------------------------------

using namespace atcoder;

int main() {
    ll H, W, N;
    cin >> H >> W >> N;
    vvl islands(N);
    rep(i, N) {
        ll x, y;
        cin >> x >> y;
        islands[i] = {x - 1, y - 1};
    }

    vvvl W_islands(W);
    rep(i, W) {
        W_islands[i] = {};
    }
    rep(i, N) {
        vl x = islands[i];
        W_islands[x[1]].push_back({x[0], i});
    }

    rep(i, W) {
        sort(W_islands[i].begin(), W_islands[i].end());
    }

    vvl W_islands_heights(W);
    rep(i, W) {
        vvl x = W_islands[i];
        W_islands_heights[i] = {};
        rep(j, x.size()) {
            vl y = x[j];
            W_islands_heights[i].push_back(y[0]);
        }
    }

    vvl events;
    rep(i, W) {
        rep(j, W_islands[i].size()) {
            vl x = W_islands[i][j];
            if (i > 0) {
                vl wihs = W_islands_heights[i - 1];
                ll touch_idx = lower_bound(wihs.begin(), wihs.end(), x[0]) - wihs.begin();
                if (touch_idx < wihs.size()) {
                    vl target_x = W_islands[i - 1][touch_idx];
                    events.push_back({target_x[0] - x[0], x[1], target_x[1]});
                }
            }

            if (i < W - 1) {
                vl wihs = W_islands_heights[i + 1];
                ll touch_idx = lower_bound(wihs.begin(), wihs.end(), x[0]) - wihs.begin();
                if (touch_idx < wihs.size()) {
                    vl target_x = W_islands[i + 1][touch_idx];
                    events.push_back({target_x[0] - x[0], x[1], target_x[1]});
                }
            }

            if (W_islands[i].size() > j + 1) {
                vl target_x = W_islands[i][j + 1];
                events.push_back({target_x[0] - x[0] - 1, x[1], target_x[1]});
            }
        }
    }

    sort(events.begin(), events.end());

    dsu unionfind(N);
    rep(i, events.size()) {
        vl event = events[i];
        unionfind.merge(event[1], event[2]);
        if (unionfind.size(event[1]) == N) {
            cout << event[0] << endl;
            return 0;
        }
    }

    cout << -1 << endl;
}
