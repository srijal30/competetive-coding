#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool pathExists(int w, int h, vector<vector<int>> & portals) { 
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