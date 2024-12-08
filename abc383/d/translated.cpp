// 以下はPythonコードのオリジナル
/*
from math import sqrt, floor

N = int(input())
root_max = floor(sqrt(N))
ans = 0

for i in range(1, root_max + 1):
    if sqrt(i) % 1 == 0:
        continue

    for j in range(2, floor(sqrt(i)) + 1):
        if i % j == 0:
            test = i // j
            last = j
            break
    else:
        continue

    for j in range(last, floor(sqrt(i)) + 1):
        if test % j == 0:
            break
    else:
        # print(i ** 2)
        ans += 1

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 57]
for i in prime:
    if i ** 8 <= N:
        ans += 1
    else:
        break

print(ans)

*/

// 以下はC++での翻訳（コンテスト時間外にChatGPTを使用、ルールも遵守）
// 全てintだと極端に少なくなったので、オーバーフローを心配してlong longに変えた
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    long long N;
    cin >> N;

    long long root_max = floor(sqrt(N));
    long long ans = 0;

    for (long long i = 1; i <= root_max; ++i) {
        if (sqrt(i) == floor(sqrt(i))) {
            continue;
        }

        long long test = 0, last = 0;
        bool found = false;
        for (long long j = 2; j <= floor(sqrt(i)); ++j) {
            if (i % j == 0) {
                test = i / j;
                last = j;
                found = true;
                break;
            }
        }
        if (!found) continue;

        found = false;
        for (long long j = last; j <= floor(sqrt(i)); ++j) {
            if (test % j == 0) {
                found = true;
                break;
            }
        }
        if (!found) {
            ans += 1;
        }
    }

    vector<long long> prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 57};
    for (long long p : prime) {
        if (pow(p, 8) <= N) {
            ans += 1;
        } else {
            break;
        }
    }

    cout << ans << endl;
    return 0;
}
