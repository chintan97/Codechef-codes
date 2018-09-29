#include <iostream>
#include <algorithm>
#include <bits/stdc++.h> 
using namespace std;

int main() {
	// your code goes here
	int n, m, max, temp, save_m;
	vector<int> A;
	cin>>n>>m;
	while (n){
		cin>>temp;
		A.push_back(temp);
		if (temp > max)
			max = temp;
		n--;
	}
	save_m = m+max;
	sort(A.begin(), A.end());
	while(m){
		A.front()++;
		if (*A.begin() > *(A.begin()+1))
			sort(A.begin(), A.end());
		m--;
	}
	cout<<A.back()<<" "<<save_m;
	return 0;
}
