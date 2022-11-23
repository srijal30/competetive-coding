#include <iostream>
#include <vector>
#include <string>

using namespace std;

/* Return the shortest for a person to get to the finish destination */
vector<int> evacuate(int n, int k, string order[], int duration[], string sfx[][3]) {
    vector<int> v;
    return v;
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T, n, k;
    cin >> T;
    while(T--)
    {
        cin >> n >> k;
        string order[n]; //The order in which the portals turn on
        int duration[n]; //The time in which each portal stays on
        string sfx[k][3];
        for(int i = 0; i < n; i++)
        {
            cin >> order[i];
        }
        
        for (int i = 0; i < n; i++) cin >> duration[i];
        
        for (int i = 0; i < k; i++)
        {
            cin >> sfx[i][0] >> sfx[i][1] >> sfx[i][2];
        }
        
        vector<int> res = evacuate(n, k, order, duration, sfx);
        
        for (int i = 0; i < res.size(); i++) 
        {
            cout << res[i] << endl;
        }
    }
}