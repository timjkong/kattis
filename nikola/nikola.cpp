#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

const int INF = 1e9;

int n;
int memo[1001][1001];
vector<int> cost;

int dp(int i, int jump) {
    if (i < 0 || i >= n) return INF;
    if (i == n - 1) return cost[i];
    int &ans = memo[i][jump];
    if (ans != -1) return ans;
    if (jump == 0) return ans = dp(i + 1, 1);
    return ans = cost[i] + min(dp(i + jump + 1, jump + 1), dp(i - jump, jump));
}

int main() {
    cin >> n;
    cost.assign(n, 0);
    for (int i = 0; i < n; i++) cin >> cost[i];
    memset(memo, -1, sizeof memo);
    cout << dp(0, 0);
}
