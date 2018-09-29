#include<iostream>
#include<vector>

using namespace std;

int main(){
	vector<long long int> S, P;
	long long int N, save_N, D, i, best_pos = 1, current_points, best_points, lowest_points, temp_pos=1;
	
	cin>>N>>D;
	save_N = N;
	while (save_N--){
		cin>>i;
		S.push_back(i);
	}
	save_N = N;
	while (save_N--){
		cin>>i;
		P.push_back(i);
	}
	current_points = S[D-1];
	best_points = P[0] + current_points;
	lowest_points = P.back();
	
	for (auto i=S.begin(); i!=S.end(); i++){
		if (*i <= best_points && (*i + lowest_points) < best_points){
			break;
		}
		else if (*i <= best_points && (*i + lowest_points) == best_points){
			lowest_points = P[N-temp_pos-1];
			while (S[temp_pos] <= best_points && (S[temp_pos] + lowest_points) >= best_points){
				if (S[temp_pos] == S[D-1]){
					temp_pos++;
					continue;
				}
				if ((S[temp_pos] + lowest_points) > best_points)
					best_pos++;
				temp_pos++;
				lowest_points = P[N-temp_pos-1];
			}
			break;
		}
		else{
			best_pos++;
		}
	}
	cout<<best_pos;
	return 0;
}
