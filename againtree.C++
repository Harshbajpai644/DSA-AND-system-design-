#include <iostream>
#include <vector>
#include <map>

using namespace std;

long long n, k;
long long a[100005];
vector<int> adj[100005];
vector<long long> b;
long long MOD = 1e9 + 7;

map<long long, long long> solve(int u, int p) {
    map<long long, long long> dp;
    dp[a[u]] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        map<long long, long long> next_dp;
        map<long long, long long> child_dp = solve(v, u);

        for (auto const& [u_xor, u_count] : dp) {
            for (auto const& [v_xor, v_count] : child_dp) {
                long long ways = (u_count * v_count) % MOD;
                
                next_dp[u_xor ^ v_xor] = (next_dp[u_xor ^ v_xor] + ways) % MOD;

                bool can_cut = false;
                for (long long target : b) {
                    if (v_xor == target) {
                        can_cut = true;
                        break;
                    }
                }
                if (can_cut) {
                    next_dp[u_xor] = (next_dp[u_xor] + ways) % MOD;
                }
            }
        }
        dp = next_dp;
    }
    return dp;
}

void solve_task() {
    int n_val;
    cin >> n_val >> k;
    for (int i = 1; i <= n_val; i++) {
        adj[i].clear();
    }
    b.clear();

    for (int i = 0; i < n_val - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 1; i <= n_val; i++) cin >> a[i];
    for (int i = 0; i < k; i++) {
        long long val;
        cin >> val;
        b.push_back(val);
    }

    map<long long, long long> res = solve(1, 0);
    long long ans = 0;
    for (long long target : b) {
        if (res.count(target)) {
            ans = (ans + res[target]) % MOD;
        }
    }
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve_task();
    }
    return 0;
}