#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> W, D;

// 移動方向
const vector<pair<char, pair<int, int>>> MOVINGS = {
    {'U', {-1, 0}},
    {'D', {1, 0}},
    {'L', {0, -1}},
    {'R', {0, 1}}
};

struct Answer {
    int score = -1;
    vector<string> steps;

    void pick() { steps.push_back("1"); }
    void drop() { steps.push_back("2"); }
    void move(char move, int times = 1) {
        if (times > 0) {
            for (int i = 0; i < times; ++i) steps.push_back(string(1, move));
        } else if (times < 0) {
            char rev;
            if (move == 'U') rev = 'D';
            else if (move == 'D') rev = 'U';
            else if (move == 'L') rev = 'R';
            else rev = 'L';
            for (int i = 0; i < -times; ++i) steps.push_back(string(1, rev));
        }
    }
    int calc_score() {
        score = N * N + 2 * N * N * N - (int)steps.size();
        return score;
    }
    void print() {
        for (auto &s : steps) cout << s << "\n";
    }
};

Answer ans_init() {
    Answer ans;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (W[i][j] == 0) continue;
            ans.move('R', j);
            ans.move('D', i);
            ans.pick();
            ans.move('L', j);
            ans.move('U', i);
        }
    }
    return ans;
}

Answer ans_random_nearests() {
    Answer ans;
    vector<vector<bool>> picked(N, vector<bool>(N, false));
    int start_random = rand() % 3;
    vector<pair<int, int>> starts;
    if (start_random == 0) {
        for (int ij = 0; ij < N * 2; ++ij) {
            for (int si = 0; si < N; ++si) {
                int sj = ij - si;
                if (0 <= sj && sj < N) starts.emplace_back(si, sj);
            }
        }
    } else if (start_random == 1) {
        for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) starts.emplace_back(i, j);
    } else {
        for (int j = 0; j < N; ++j) for (int i = 0; i < N; ++i) starts.emplace_back(i, j);
    }
    for (auto &start : starts) {
        int si = start.first, sj = start.second;
        if (W[si][sj] == 0 || picked[si][sj]) continue;
        picked[si][sj] = true;
        vector<pair<int, int>> pick_boxes = { {0, 0}, {si, sj} };
        int sum_w = W[si][sj];
        int sum_dist = si + sj;
        int i = si, j = sj;
        string before_move = "-";
        while (true) {
            if (i == N - 1 && j == N - 1) break;
            char move;
            double r = (double)rand() / RAND_MAX;
            vector<double> weights = { pow(19 - i, 0.5), pow(19 - j, 0.5), 1 + pow(r, 2) * 0.2, 1 + pow(r, 2) * 0.2 };
            vector<char> moves = { 'D', 'R', 'U', 'L' };
            double total = 0;
            for (auto w : weights) total += w;
            double x = ((double)rand() / RAND_MAX) * total;
            int idx = 0;
            for (; idx < 4; ++idx) {
                if (x < weights[idx]) break;
                x -= weights[idx];
            }
            move = moves[idx];
            int di = 0, dj = 0;
            for (auto &mv : MOVINGS) if (mv.first == move) { di = mv.second.first; dj = mv.second.second; }
            char rev = (move == 'U' ? 'D' : move == 'D' ? 'U' : move == 'L' ? 'R' : 'L');
            if (!(0 <= i + di && i + di < N && 0 <= j + dj && j + dj < N) || string(1, rev) == before_move) continue;
            i += di; j += dj;
            if (picked[i][j] || D[i][j] <= sum_w * sum_dist) continue;
            picked[i][j] = true;
            int dist = abs(i - pick_boxes.back().first) + abs(j - pick_boxes.back().second);
            pick_boxes.emplace_back(i, j);
            sum_w += W[i][j];
            sum_dist += dist;
        }
        ans.move('D', pick_boxes.back().first);
        ans.move('R', pick_boxes.back().second);
        for (int k = (int)pick_boxes.size() - 1; k > 0; --k) {
            ans.pick();
            ans.move('U', pick_boxes[k].first - pick_boxes[k - 1].first);
            ans.move('L', pick_boxes[k].second - pick_boxes[k - 1].second);
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;
    W.assign(N, vector<int>(N));
    D.assign(N, vector<int>(N));
    for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) cin >> W[i][j];
    for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) cin >> D[i][j];
    srand(time(0));
    Answer best_ans = ans_init();
    best_ans.calc_score();
    int update_count = 0, repeat_count = 0;
    double start = clock();
    while ((clock() - start) / CLOCKS_PER_SEC < 1.9) {
        Answer ans = ans_random_nearests();
        if (ans.calc_score() > best_ans.score) {
            best_ans = ans;
            update_count++;
        }
        repeat_count++;
    }
    best_ans.print();
    cerr << "repeat_count = " << repeat_count << endl;
    cerr << "update_count = " << update_count << endl;
    cerr << "score = " << best_ans.score << endl;
    return 0;
}
