// 原文Pythonコード（AtCoderの規約により必ず先頭に含める）
//
// from atcoder.dsu import DSU
// import heapq
//
// def manhattan(i: int, j: int):
//     return abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])
//
// class Dist:
//     def __init__(self, i: int, j: int):
//         self.dist = manhattan(i, j)
//         self.i = i
//         self.j = j
//
//     def __lt__(self, other):
//         assert isinstance(other, Dist)
//         return self.dist < other.dist
//
// N, Q = [int(x) for x in input().split()]
// nodes = []
// for _ in range(N):
//     nodes.append(tuple(int(x) for x in input().split()))
//
// last_N = N
// queries = []
// for _ in range(Q):
//     query = tuple(int(x) for x in input().split())
//     queries.append(query)
//     if query[0] == 1:
//         last_N += 1
//
// uf = DSU(last_N)
//
// dists = []
// for i in range(N):
//     for j in range(i + 1, N):
//         dists.append(Dist(i, j))
//
// heapq.heapify(dists)
//
// for query in queries:
//     if query[0] == 1:
//         a, b = query[1], query[2]
//         nodes.append((a, b))
//         for i in range(len(nodes) - 1):
//             distance = manhattan(len(nodes) - 1, i)
//             heapq.heappush(dists, Dist(i, len(nodes) - 1))
//
//     elif query[0] == 2:
//         nearest_distance = 10 ** 18
//         ok = False
//         while len(dists) > 0:
//             d = heapq.heappop(dists)
//             distance, i, j = d.dist, d.i, d.j
//
//             if uf.same(i, j):
//                 continue
//
//             if distance > nearest_distance:
//                 heapq.heappush(dists, Dist(i, j))
//                 break
//
//             if nearest_distance == 10 ** 18:
//                 nearest_distance = distance
//
//             uf.merge(i, j)
//             ok = True
//
//         if not ok:
//             print(-1)
//             continue
//
//         assert nearest_distance < 10 ** 18
//         print(nearest_distance)
//
//     else:
//         u, v = query[1] - 1, query[2] - 1
//         print("Yes" if uf.same(u, v) else "No")

// ↓ C++への変換コード（同等アルゴリズム）↓

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;

struct DSU {
    vector<int> parent, size;
    DSU(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int leader(int x) {
        if (parent[x] == x) return x;
        return parent[x] = leader(parent[x]);
    }
    bool same(int x, int y) {
        return leader(x) == leader(y);
    }
    bool merge(int x, int y) {
        x = leader(x), y = leader(y);
        if (x == y) return false;
        if (size[x] < size[y]) swap(x, y);
        parent[y] = x;
        size[x] += size[y];
        return true;
    }
};

vector<pii> nodes;

ll manhattan(int i, int j) {
    return abs(nodes[i].first - nodes[j].first) + abs(nodes[i].second - nodes[j].second);
}

struct Dist {
    ll dist;
    int i, j;
    Dist(int i_, int j_) : dist(manhattan(i_, j_)), i(i_), j(j_) {}
    bool operator>(const Dist& other) const {
        return dist > other.dist;
    }
};

int main() {
    int N, Q;
    cin >> N >> Q;

    nodes.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> nodes[i].first >> nodes[i].second;
    }

    int last_N = N;
    vector<tuple<int, int, int>> queries;
    for (int i = 0; i < Q; ++i) {
        int t, x, y;
        cin >> t;
        if (t == 2) {
            x = -1;
            y = -1;
        } else {
            cin >> x >> y;
        }
        queries.emplace_back(t, x, y);
        if (t == 1) last_N++;
    }

    DSU uf(last_N);

    priority_queue<Dist, vector<Dist>, greater<Dist>> dists;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            dists.emplace(i, j);
        }
    }

    for (auto& q : queries) {
        int type, a, b;
        tie(type, a, b) = q;

        if (type == 1) {
            nodes.emplace_back(a, b);
            int new_idx = nodes.size() - 1;
            for (int i = 0; i < new_idx; ++i) {
                dists.emplace(i, new_idx);
            }
        } else if (type == 2) {
            ll nearest_distance = 1e18;
            bool ok = false;
            while (!dists.empty()) {
                Dist d = dists.top(); dists.pop();
                ll distance = d.dist;
                int i = d.i, j = d.j;

                if (uf.same(i, j)) continue;

                if (distance > nearest_distance) {
                    dists.push(d);
                    break;
                }

                if (nearest_distance == (ll)1e18) {
                    nearest_distance = distance;
                }

                uf.merge(i, j);
                ok = true;
            }

            if (!ok) {
                cout << -1 << endl;
                continue;
            }

            assert(nearest_distance < (ll)1e18);
            cout << nearest_distance << endl;
        } else {
            int u = a - 1, v = b - 1;
            cout << (uf.same(u, v) ? "Yes" : "No") << endl;
        }
    }

    return 0;
}
