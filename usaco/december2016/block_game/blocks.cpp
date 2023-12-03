#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>

using namespace std;

bool isUnique(char c, string str, char* used){
	for(int i = 0; i < str.length(); i++){
		if(str[i] == c  && used[i] == 0){
			used[i]++;
			return false;
		}
	}
	return true;
}

int main(){
	freopen("blocks.in", "r", stdin);
	freopen("blocks.out", "w", stdout);
	
	int letters[26];
	int n; cin >> n;
	memset(letters, 0, 26*sizeof(int));

	for(int i = 0; i < n; i++){
		string a, b; cin >> a >> b;
		//add all letters required for first
		for(int j = 0; j < a.length(); j++)
			letters[a[j]-97]++;
		//add the unique letters for second
		char used[10]; memset(used, 0, 10);
		for(int j = 0; j < b.length(); j++)
			if(isUnique(b[j], a, used)) letters[b[j]-97]++;
	}

	for(int i = 0; i < 26; i++)
		cout << letters[i] << "\n";
}
