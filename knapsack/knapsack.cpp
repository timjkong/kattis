#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int n, c;
vector<int> value(2001), weight(2001);
vector< vector<int> > dp;

void knapsack() {
    for (int w = weight[0]; w <= c; w++) {
        dp[0][w] = value[0];
    }
    for (int i = 1; i < n; i++) {
        for (int w = 0; w <= c; w++) {
            dp[i][w] = dp[i - 1][w];
            if (weight[i] <= w) {
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight[i]] + value[i]);
            }
        }
    }
}

void print_knapsack() {
    vector<int> items;
    for (int i = n - 1; i > 0; i--) {
        if (c <= 0) break;
        if (dp[i][c] > dp[i - 1][c]) {
            items.push_back(i);
            c -= weight[i];
        }
    }
    if (weight[0] <= c) items.push_back(0);
    cout << items.size() << '\n';
    for (int item : items) {
        cout << item << ' ';
    }
}


int main() {
    ios::sync_with_stdio(false);
    while (cin >> c >> n) {
        for (int i = 0; i < n; i++) {
            cin >> value[i] >> weight[i];
        }
        dp.assign(n, vector<int>(c + 1, 0));
        knapsack();
        print_knapsack();
        cout << '\n';
    }
}
