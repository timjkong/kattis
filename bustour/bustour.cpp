#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <list>
#include <math.h>
#include <climits>
#include <tuple>
#include <cstring>

using namespace std;

typedef long long ll;

#define LSOne(S) ((S) & -(S))

const int MAX_n = 21;
const int INF = 1e9;

int n;
int dist[MAX_n][MAX_n];
ll memo_hq[MAX_n][1<<(MAX_n-1)];
ll memo_attraction[MAX_n][1<<(MAX_n-1)];

// min dist starting at u, visiting all hotels in mask (on bits), and going back to hq
// equivalent to dist starting at hq and ending at u
ll dp_hq(int u, int mask) {
    if (mask == 0) return dist[u][0];
    ll &ans = memo_hq[u][mask];
    if (ans != -1) return ans;
    ans = INF;
    int m = mask;
    while (m) {
        int two_pow_v = LSOne(m);
        int v = __builtin_ctz(two_pow_v) + 1;
        ans = min(ans, dist[u][v] + dp_hq(v, mask^two_pow_v));
        m -= two_pow_v;
    }
    return ans;
}

// min dist starting at u, visiting all hotels in mask (on bits), and going back to attraction
ll dp_attraction(int u, int mask) {
    if (mask == 0) return dist[u][n - 1];
    ll &ans = memo_attraction[u][mask];
    if (ans != -1) return ans;
    ans = INF;
    int m = mask;
    while (m) {
        int two_pow_v = LSOne(m);
        int v = __builtin_ctz(two_pow_v) + 1;
        ans = min(ans, dist[u][v] + dp_attraction(v, mask^two_pow_v));
        m -= two_pow_v;
    }
    return ans;
}

int main() {
    int TC = 1;
    int m;
    while (cin >> n >> m) {
        // init dist
        for (int u = 0; u < n; u++) {
            for (int v = 0; v < n; v++) {
                dist[u][v] = INF;
            }
            dist[u][u] = 0;
        }
        for (int i = 0; i < m; i++) {
            int u, v, t; cin >> u >> v >> t;
            dist[u][v] = t;
            dist[v][u] = t;
        }
        // floyd-warshall
        for (int k = 0; k < n; ++k)
            for (int u = 0; u < n; ++u)
                for (int v = 0; v < n; ++v)
                    dist[u][v] = min(dist[u][v], dist[u][k]+dist[k][v]);

        // edge case: 1 hotel
        if (n == 3) {
            printf("Case %i: %i\n", TC, 2 * (dist[0][1] + dist[1][2]));
            TC++;
            continue;
        }

        memset(memo_hq, -1, sizeof memo_hq);
        memset(memo_attraction, -1, sizeof memo_attraction);

        ll shortest_route = INT_MAX;

        for (int mask = 0; mask < (1 << (n - 2)); mask++) {
            // only try subsets containing half the hotels
            if (__builtin_popcount(mask) != (n - 2) / 2) continue;
            int complement = ((1 << (n - 2)) - 1) ^ mask;
            // try all possible last hotels in mask (going to attraction)
            for (int i = 1; i < n - 1; i++) {
                // try all possible first hotels in mask (coming back to hq)
                for (int j = 1; j < n - 1; j++) {
                    if (!(mask & (1 << (i - 1))) || !(mask & (1 << (j - 1)))) continue;
                    // hq to i through hotels in mask
                    // + i to attraction through hotels in complement
                    // + attraction to j through hotels in mask
                    // + j to hq through hotels in complement
                    ll route = dp_hq(i, mask ^ (1 << (i - 1))) + dp_attraction(i, complement) + 
                                dp_attraction(j, mask ^ (1 << (j - 1))) + dp_hq(j, complement);
                    shortest_route = min(shortest_route, route);
                }
            }
        }

        printf("Case %i: %lld\n", TC, shortest_route);
        TC++;
    }
}
