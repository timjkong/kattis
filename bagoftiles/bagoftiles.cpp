#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef long long ll;

int g, m, n, t;
vector<int> labels(31);
ll memo[31][31][10001];


ll dp(int i, int count, int value) {
    if (value == 0) return count == n ? 1 : 0;
    if (i == m || count > n || value < 0) return 0;

    ll &ans = memo[i][count][value];
    if (ans != -1) return ans;
    ans = dp(i + 1, count, value) + dp(i + 1, count + 1, value - labels[i]);
    return ans;
}

ll memo_comb[31][31];
ll comb(int n, int r){
    if (r == 0 || n == r) return 1;
    if (n < r) return 0;
    if (memo_comb[n][r] != -1) return memo_comb[n][r];
    return memo_comb[n][r] =  comb(n - 1, r - 1) + comb(n - 1, r);
}


int main() {
    memset(memo_comb, -1, sizeof(memo_comb));
    cin >> g;
    for (int g_id = 1; g_id <= g; g_id++) {
        cin >> m;
        labels.resize(m);
        for (int i = 0; i < m; i++) {
            cin >> labels[i];
        }
        cin >> n >> t;
        memset(memo, -1, sizeof(memo));
        ll winning_odds = dp(0, 0, t);
        ll losing_odds = comb(m, n) - winning_odds;
        printf("Game %d -- %lld : %lld\n", g_id, winning_odds, losing_odds);
    }
}
