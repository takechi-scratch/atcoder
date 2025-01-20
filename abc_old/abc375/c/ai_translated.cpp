// PythonのTLE解答をChatGPTに翻訳してもらった。これでも3TLE。

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// サブマトリックスを90度回転させる関数
vector<vector<char>> kaiten(const vector<vector<char>>& list2d) {
    int n = list2d.size();
    vector<vector<char>> rotated(n, vector<char>(n));

    // 90度時計回りに回転させる処理
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            rotated[j][n - i - 1] = list2d[i][j];
        }
    }
    return rotated;
}

int main() {
    int N;
    cin >> N;

    vector<vector<char>> A(N, vector<char>(N));

    // 入力を読み込む
    for (int i = 0; i < N; ++i) {
        string line;
        cin >> line;
        for (int j = 0; j < N; ++j) {
            A[i][j] = line[j];
        }
    }

    // 四隅の部分を回転させる処理
    for (int i = 0; i < N / 2; ++i) {
        int sub_size = N - 2 * i; // サブマトリックスのサイズ

        // サブマトリックスの作成
        vector<vector<char>> submatrix(sub_size, vector<char>(sub_size));
        for (int x = 0; x < sub_size; ++x) {
            for (int y = 0; y < sub_size; ++y) {
                submatrix[x][y] = A[i + x][i + y];
            }
        }

        // サブマトリックスの回転
        vector<vector<char>> kaiten_results = kaiten(submatrix);

        // 回転後のサブマトリックスを元の行列に戻す
        for (int x = 0; x < sub_size; ++x) {
            for (int y = 0; y < sub_size; ++y) {
                A[i + x][i + y] = kaiten_results[x][y];
            }
        }
    }

    // 結果を出力
    for (const auto& row : A) {
        for (const auto& ch : row) {
            cout << ch;
        }
        cout << endl;
    }

    return 0;
}
