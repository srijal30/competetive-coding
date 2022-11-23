#include <bits/stdc++.h>

using namespace std;

bool pathExists(int w, int h, vector<vector<int>> & portals) {
    int n = portals.size();
    vector<vector<int>> adj(n);

    bool can_go = false; int start, left_most_x = INT_MAX;
    vector<vector<int>> color_org(10000), xcoord_org(10000);
    for(int i = 0; i < n; i++) {
        color_org[portals[i][2]].push_back(i);
        xcoord_org[portals[i][0]].push_back(i);
        if(portals[i][1] == 0) {
            can_go = true;
            if(p1[0] < left_most_x) {
                start = i;
                left_most_x = i;
            }
        }
    }

    for(int i = 1; i < n; i++) {
        adj[color_org[i]].push_back(color_org[i - 1]);
        adj[color_org[i - 1]].push_back(color_org[i]);
    }

    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            vector<int> p1 = portals[i], p2 = portals[j];
            if(p1[2] == p2[2]) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
            else if(p1[1] == p2[1]) {
                if(p1[0] < p2[0]) adj[i].push_back(j);
                else adj[j].push_back(i);   
            }
            
            if(p1[1] == 0) {
                can_go = true;
                if(p1[0] < left_most_x) {
                    start = i;
                    left_most_x = i;
                }
            }
        }
    }

    cout << start << "\n";
    int count = 0;
    for(auto v : adj) {
        cout << count++ << ": ";
        for(int i : v) cout << i << " ";
        cout << "\n";
    }

    if(can_go) {
        queue<int> q;
        vector<bool> visited(n);
        q.push(start);
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            if(portals[curr][1] == h - 1) return true;
            visited[curr] = true;
            for(int node : adj[curr]) {
                if(!visited[node]) q.push(node);
            }
            for(int node : xcoord_org[portals[curr][0]]) {
                if(!visited[node]) q.push(node);
            }
        }
    }
    return false;
}

 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int W, H; cin >> W >> H;
        int N; cin >> N;
        vector<vector<int>> portals (N, vector<int>(3,0));
        for (int i = 0 ; i < N; i++) {
            cin >> portals[i][0] >> portals[i][1] >> portals[i][2];
        }
        bool ans = pathExists(W, H, portals);
        cout << (ans ? "true" : "false") << '\n';
    }
}