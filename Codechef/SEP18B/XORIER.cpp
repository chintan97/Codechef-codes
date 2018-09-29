#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<bits/stdc++.h>
using namespace std;

vector<long int> p;
long int p_computed_l = 2, p_computed_u = 3;
int prime(long int);
int prime_vector(long int);
int main(){
	int T;
	long int N, i, j, iterator, XOR_i_j, count=0, temp, temp1, temp2, k;
	long int A[1000000];
	p.push_back(2);
	p.push_back(3);
	cin>>T;
	while (T > 0){
		count = 0;
		cin>>N;
		for (i=0; i<N; i++){
			cin>>A[i];
		}
		for (i=1; i<N; i++){
			for (j=0; j<i; j++){
				XOR_i_j = A[i] ^ A[j];
				if (XOR_i_j%2 != 0){
					continue;
				}
				else{
					iterator = 0;
					temp = XOR_i_j/2;
					
					while (p[iterator] <= temp){
						temp1 = p[iterator];
						temp2 = XOR_i_j - p[iterator];
						if (prime_vector(temp2) == 2){
							count++;
							break;
						}
						iterator++;
					}
				}
			}
		}
		cout<<count<<"\n";
		T--;
	}
}



int prime(long int check_prime){
	long int ite;
	if (check_prime <= 1)
		return 1;
	else{
		for (auto ite=p.begin(); *ite<ceil(sqrt(check_prime)); ite++){
			if (check_prime%*ite == 0){
				return 1;
			}
		}
		return 2;
	}
}

int prime_vector(long int check_vector){
	if (check_vector <= p_computed_u){
		if ( binary_search(p.begin(), p.end(), check_vector) ){
			return 2;
		}
		else{
			return 1;
		}
	}
	else{
		long int i = p.back();
		while (i < check_vector){
			if (prime(i) == 2){
				p.push_back(i);
			}
			i += 2;
		}
		p_computed_u = check_vector;
		if (prime(check_vector) == 2){
			p.push_back(check_vector);
			return 2;
		}
		else{
			return 1;
		}
	}
}
