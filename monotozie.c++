#include <iostream>
#include <vector>
#include <bitset>
#include <set>

using namespace std;

const int MAXN = 25005;
bitset<MAXN> rows[MAXN];
int row_counts[MAXN];

struct RowComp {
    bool operator()(int a, int b) const {
        if (row_counts[a] != row_counts[b]) {
            return row_counts[a] < row_counts[b];
        }
        return a < b;
    }
};

bool is_subset(int a, int b) {
    return (rows[a] & rows[b]) == rows[a];
}

void solve() {
    int n, q;
    if (!(cin >> n >> q)) return;

    for (int i = 1; i <= n; i++) {
        rows[i].reset();
        row_counts[i] = 0;
    }

    set<int, RowComp> chain;
    for (int i = 1; i <= n; i++) {
        chain.insert(i);
    }

    int bad_pairs = 0;

    auto update_bad = [&](int a, int b, int delta) {
        if (!is_subset(a, b)) bad_pairs += delta;
    };

    while (q--) {
        int r, c;
        cin >> r >> c;

        auto it = chain.find(r);
        auto nxt = next(it);
        auto prv = (it == chain.begin()) ? chain.end() : prev(it);

        if (nxt != chain.end()) update_bad(r, *nxt, -1);
        if (prv != chain.end()) update_bad(*prv, r, -1);
        if (nxt != chain.end() && prv != chain.end()) update_bad(*prv, *nxt, 1);

        chain.erase(it);
        rows[r].set(c);
        row_counts[r]++;
        
        auto res = chain.insert(r);
        it = res.first;
        nxt = next(it);
        prv = (it == chain.begin()) ? chain.end() : prev(it);

        if (nxt != chain.end()) update_bad(r, *nxt, 1);
        if (prv != chain.end()) update_bad(*prv, r, 1);
        if (nxt != chain.end() && prv != chain.end()) update_bad(*prv, *nxt, -1);

        if (bad_pairs == 0) cout << "YES\n";
        else cout << "NO\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}