#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

int n, coins[101];
int max_val;
vector<int> memo;


int canonical(int val) {
    int count = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (val == 0) break;
        if (coins[i] > val) continue;
        count += val / coins[i];
        val = val % coins[i];
    }
    return count;
}

int dp(int val) {
    if (val <= 1) return val;
    int &ans = memo[val];
    if (ans != -1) return ans;
    ans = 1e9;
    for (int c : coins) {
        if (c > val) break;
        ans = min(ans, 1 + dp(val - c));
    }
    return ans;
}

string is_canonical() {
    for (int val = max_val - 1; val > 1; val--) {
        if (dp(val) != canonical(val)) return "non-canonical";
    }
    return "canonical";
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> coins[i];
    max_val = coins[n - 1] + coins[n - 2];
    memo.assign(max_val, -1);
    cout << is_canonical();
}
