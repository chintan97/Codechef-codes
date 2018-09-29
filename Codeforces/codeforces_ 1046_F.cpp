#include<iostream>
#include<vector>
#include<math.h>

using namespace std;

int main(){
	vector<long long int> a;
	long long int N, f, x, x_f, i, count=0;
	
	cin>>N;
	while (N--){
		cin>>i;
		a.push_back(i);
	}
	cin>>x>>f;
	x_f = x + f;
	
	for (auto i=a.begin(); i!=a.end(); i++){
		if (*i > x){
			N = (*i)/x_f;
			if ((*i - (x_f*N)) <= x)
				count += f*N;
			else
				count += f*N + f;
		}
	}
	cout<<count;
	
	return 0;
}
