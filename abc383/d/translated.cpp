// 元のPythonコード:
// from math import sqrt, floor
//
// N = int(input())
// ans = 0
//
// for i in range(1, floor(sqrt(N)) + 1):
//     if sqrt(i) % 1 == 0:
//         continue
//
//     for j in range(2, floor(sqrt(i)) + 1):
//         if i % j == 0:
//             test = i // j
//             break
//     else:
//         continue
//
//     for j in range(2, floor(sqrt(i)) + 1):
//         if test % j == 0:
//             break
//     else:
//         ans += 1
//
// print(ans)

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ans = 0;

    for (int i = 1; i <= floor(sqrt(N)); ++i) {
        if (sqrt(i) == floor(sqrt(i))) {
            continue;
        }

        int test = -1;
        for (int j = 2; j <= floor(sqrt(i)); ++j) {
            if (i % j == 0) {
                test = i / j;
                break;
            }
        }
        if (test == -1) {
            continue;
        }

        bool is_prime = true;
        for (int j = 2; j <= floor(sqrt(test)); ++j) {
            if (test % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            ++ans;
        }
    }

    cout << ans << endl;
    return 0;
}
