#include <iostream>
#include <tuple>
#include <vector>

using namespace std;


int main(){
	typedef tuple<char, int, int> cow;
	vector<cow> cows;
	int n; cin >> n;

	for(int i = 0; i < n; n++){
		int x, y; char c; cin >> c >> a >> b;
		cows.push_back(make_tuple(c,a,b));
	}
	
	return 0;
}
