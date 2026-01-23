#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll power(ll base, ll exp, ll mod) {
    ll res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

ll modInverse(ll n, ll mod) {
    return power(n, mod - 2, mod);
}

struct DSU {
    vector<int> parent;
    int components;
    DSU(int n) {
        parent.resize(n + 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
        components = n;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
        }
    }
};

void solve() {
    int n;
    ll m, p;
    if (!(cin >> n >> m >> p)) return;

    vector<pair<int, int>> subs;
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            subs.push_back({i, j});
        }
    }

    int sz = subs.size();
    ll total_expected_beauty = 0;
    ll inv_m = modInverse(m, p);

    for (int i = 0; i < sz; i++) {
        for (int j = i; j < sz; j++) {
            DSU dsu(n);
            auto s1 = subs[i];
            auto s2 = subs[j];

            for (int k = 0; k <= (s1.second - s1.first) / 2; k++) {
                dsu.unite(s1.first + k, s1.second - k);
            }
            for (int k = 0; k <= (s2.second - s2.first) / 2; k++) {
                dsu.unite(s2.first + k, s2.second - k);
            }

            ll prob = power(m, dsu.components, p) * power(inv_m, n, p) % p;
            
            if (i == j) {
                total_expected_beauty = (total_expected_beauty + prob) % p;
            } else {
                total_expected_beauty = (total_expected_beauty + 2 * prob) % p;
            }
        }
    }

    cout << total_expected_beauty << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}