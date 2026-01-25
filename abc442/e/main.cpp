// GitHub CopilotでPythonコードから変換

#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-8;

struct Pair {
    long long x;
    long long y;
    int plus;

    Pair(long long x = 0, long long y = 0, int plus = 0) : x(x), y(y), plus(plus) {}
};

int shogen(const Pair& a) {
    if (a.x > 0 && a.y >= 0) {
        return 1 + a.plus * 4;
    }
    if (a.x <= 0 && a.y > 0) {
        return 2 + a.plus * 4;
    }
    if (a.x < 0 && a.y <= 0) {
        return 3 + a.plus * 4;
    }
    if (a.x >= 0 && a.y < 0) {
        return 4 + a.plus * 4;
    }
    return 0;
}

int compare(const Pair& a, const Pair& b) {
    int a_s = shogen(a);
    int b_s = shogen(b);
    if (a_s != b_s) {
        return (a_s < b_s) ? -1 : 1;
    }

    int ans_reverse = (a_s % 2) * 2 - 1;

    long long a_cp = abs(a.y) * abs(b.x);
    long long b_cp = abs(a.x) * abs(b.y);
    if (a_cp == b_cp) {
        return 0;
    } else {
        return (a_cp < b_cp) ? -1 * ans_reverse : 1 * ans_reverse;
    }
}

bool compareLess(const Pair& a, const Pair& b) {
    return compare(a, b) < 0;
}

int main() {
    int N, Q;
    cin >> N >> Q;

    vector<vector<int>> monsters(N, vector<int>(2));
    for (int i = 0; i < N; i++) {
        cin >> monsters[i][0] >> monsters[i][1];
    }

    vector<Pair> monster_args;
    vector<Pair> monster_args_bs;

    for (int i = 0; i < N; i++) {
        monster_args.push_back(Pair(monsters[i][0], monsters[i][1]));
        monster_args_bs.push_back(Pair(monsters[i][0], monsters[i][1]));
        monster_args_bs.push_back(Pair(monsters[i][0], monsters[i][1], 1));
    }

    sort(monster_args_bs.begin(), monster_args_bs.end(), compareLess);

    for (int i = 0; i < Q; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;

        Pair start = monster_args[a];
        Pair end = monster_args[b];

        if (compare(start, end) == -1) {
            start = Pair(start.x, start.y, 1);
        }

        auto right_i = upper_bound(monster_args_bs.begin(), monster_args_bs.end(), start, compareLess);
        auto left_i = lower_bound(monster_args_bs.begin(), monster_args_bs.end(), end, compareLess);

        cout << (right_i - left_i) << endl;
    }

    return 0;
}
