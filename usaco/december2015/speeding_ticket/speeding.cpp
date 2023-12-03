#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(){
	ifstream fin("speeding.in");
	ofstream fout("speeding.out");

	int n, m;
	fin >> n >> m;
	
	queue<int> segments;
	queue<int> limits;
	queue<int> stretches;
	queue<int> speeds;

	for(int i = 0; i < n; i++){
		int a, b; fin >> a >> b;
		segments.push(a); limits.push(b);
	}
		
	for(int i = 0; i < m; i++){
		int a, b; fin >> a >> b;
		stretches.push(a); speeds.push(b);
	}

	int highest = 0;
	int curSeg = segments.front();
	int curLim = limits.front();
	int curStre = stretches.front();
	int curSpe = speeds.front();
	
	while(!segments.empty()){
		highest = max(highest, curSpe-curLim);
		if(curSeg > curStre){
			curSeg -= curStre;
			stretches.pop(); speeds.pop();
			curStre = stretches.front();
			curSpe = speeds.front();
		}
		else if(curStre > curSeg){
			curStre -= curSeg;
			segments.pop(); limits.pop();
			curSeg = segments.front();
			curLim = limits.front();
		}
		else{
			segments.pop(); limits.pop(); stretches.pop(); speeds.pop();
			curSeg = segments.front();
			curLim = limits.front();
			curStre = stretches.front();
			curSpe = speeds.front();
		}
	}
	fout << highest << "\n";
	fin.close();
	fout.close();
}

