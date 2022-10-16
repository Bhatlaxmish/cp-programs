#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>
using namespace std;

// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0200r0.html
template<class Fun> class y_combinator_result {
    Fun fun_;
public:
    template<class T> explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args> decltype(auto) operator()(Args &&...args) { return fun_(std::ref(*this), std::forward<Args>(args)...); }
};
template<class Fun> decltype(auto) y_combinator(Fun &&fun) { return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun)); }


template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }

void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef NEAL_DEBUG
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

const int DIRS = 4;
const int DR[DIRS] = {-1,  0, +1,  0};
const int DC[DIRS] = { 0, +1,  0, -1};


void run_case(int test_case) {
    int R, C;
    cin >> R >> C;
    vector<string> grid(R);

    for (auto &row : grid)
        cin >> row;

    int V = R * C;
    vector<vector<int>> adj(R * C);

    auto get_index = [&](int r, int c) -> int {
        return r * C + c;
    };

    auto valid = [&](int r, int c) -> bool {
        return 0 <= r && r < R && 0 <= c && c < C;
    };

    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (grid[r][c] != '#') {
                int v = get_index(r, c);

                for (int d = 0; d < DIRS; d++) {
                    int nr = r + DR[d];
                    int nc = c + DC[d];

                    if (valid(nr, nc) && grid[nr][nc] != '#')
                        adj[v].push_back(get_index(nr, nc));
                }
            }

    vector<int> degree(V, 0);

    for (int v = 0; v < V; v++)
        degree[v] = int(adj[v].size());

    queue<int> q;

    for (int v = 0; v < V; v++)
        if (degree[v] == 1)
            q.push(v);

    while (!q.empty()) {
        int v = q.front(); q.pop();

        for (int neigh : adj[v])
            if (--degree[neigh] == 1)
                q.push(neigh);
    }

    cout << "Case #" << test_case << ": ";

    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (grid[r][c] == '^' && degree[get_index(r, c)] < 2) {
                cout << "Impossible" << '\n';
                return;
            }

    cout << "Possible" << '\n';

    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (degree[get_index(r, c)] >= 2)
                grid[r][c] = '^';

    for (auto &row : grid)
        cout << row << '\n';
}

int main() {
    int tests;
    cin >> tests;

    for (int tc = 1; tc <= tests; tc++) {
        run_case(tc);
        cout << flush;
    }
}
