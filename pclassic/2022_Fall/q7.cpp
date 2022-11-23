#include <iostream>
#include <vector>

using namespace std;

long long minTurns(long long n, long long k, long long ahfacInit, long long tienInit, vector<pair<int, int>> &edges) {
    return 0;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int t; cin >> t;
	while (t--) {
        long long n, k, ahfacInit, tienInit;
	    cin >> n >> k >> ahfacInit >> tienInit;
        vector<pair<int, int>> edges;
        for (int i = 0; i < n - 1; i++) {
            int u, v; cin >> u >> v;
            edges.push_back({u, v});
        }
		cout << minTurns(n, k, ahfacInit, tienInit, edges) << "\n";
	}	
}