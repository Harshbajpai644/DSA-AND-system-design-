#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

void solve() {
    ll n, x;
    if (!(cin >> n >> x)) return;

    ll total_safe = 0;
    ll max_gain = -2000000000000000000LL; 
    bool can_progress = false;

    for (int i = 0; i < n; ++i) {
        ll a, b, c;
        cin >> a >> b >> c;

        ll safe_for_this = (b - 1) * a;
        
        if (x - total_safe <= safe_for_this) {
            total_safe = x;
        } else {
            total_safe += safe_for_this;
        }

        ll gain = (b * a) - c;
        
        if (gain > 0) {
            can_progress = true;
            if (gain > max_gain) {
                max_gain = gain;
            }
        }
    }

    if (total_safe >= x) {
        cout << 0 << endl;
        return;
    }

    if (!can_progress) {
        cout << -1 << endl;
        return;
    }

    ll needed = x - total_safe;
    ll ans = (needed + max_gain - 1) / max_gain;

    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}