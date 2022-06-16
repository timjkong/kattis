#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int MOD = 1e9 + 7;
int V, E, Q;
int MAX_V = 4001;
int AM[4001][4001];
bool edge_flag = true;
bool transpose_flag = false;

void add_vertex() {
    for (int u = 0; u < V; u++) {
        AM[u][V] = !edge_flag;
        AM[V][u] = !edge_flag;
    }
    V++;
}

void add_edge(int u, int v) {
    if (!transpose_flag) {
        AM[u][v] = edge_flag;
    } else {
        AM[v][u] = edge_flag;
    }
}

void remove_vertex(int u) {
    for (int v = 0; v < V; v++) {
        AM[u][v] = !edge_flag;
        AM[v][u] = !edge_flag;
    }
}

void remove_edge(int u, int v) {
    if (!transpose_flag) {
        AM[u][v] = !edge_flag;
    } else {
        AM[v][u] = !edge_flag;
    }
}

void print_ans() {
    cout << V << '\n';
    for (int u = 0; u < V; u++) {
        long long out_degree = 0, vertex_hash = 0;
        long long multiplier = 1;
        for (int v = 0; v < V; v++) {
            if (u == v) continue;
            if ((!transpose_flag && AM[u][v] == edge_flag) || 
                (transpose_flag && AM[v][u] == edge_flag)) {
                vertex_hash += multiplier * v;
                vertex_hash %= MOD;
                multiplier *= 7;
                multiplier %= MOD;
                out_degree++;
            }
        }
        printf("%lld %lld\n", out_degree, vertex_hash);
    }
}

int main() {
    cin >> V >> E >> Q;
    memset(AM, 0, sizeof AM);
    while(E--) {
        int u, v; cin >> u >> v;
        AM[u][v] = edge_flag;
    }
    while (Q--) {
        int query; cin >> query;
        if (query == 1) {
            add_vertex();
        } else if (query == 2) {
            int u, v; cin >> u >> v;
            add_edge(u, v);
        } else if (query == 3) {
            int u; cin >> u;
            remove_vertex(u);
        } else if (query == 4) {
            int u, v; cin >> u >> v;
            remove_edge(u, v);
        } else if (query == 5) {
            transpose_flag = !transpose_flag;
        } else {
            edge_flag = !edge_flag;
        }
    }
    print_ans();
}
