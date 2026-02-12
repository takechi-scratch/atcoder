// https://atcoder.jp/contests/abc227/tasks/abc227_c
// 初めてC++を自力で書けた！！

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;

    long long ans = 0;
    long long A = 1;
    long long B;
    long long max_c;
    while (A * A * A <= N)
    {
        B = A;
        while (A * B * B <= N)
        {
            max_c = N / (A * B);
            ans += max_c - B + 1;
            B += 1;
        }

        A += 1;
    }
    cout << ans;

}
