#include<iostream>
#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(long long int);
int main(){
	int T;
	long int N, inc, Q1, Q2, Q, i_s, i, j, k, count, count_temp;
	long long int A[10000], AND;
	
	cin>>T;
	while (T){
		cin>>N>>Q;
		for (i=0; i<N; i++)
			cin>>A[i];
		
		for (i_s=0; i_s<Q; i_s++){
			cin>>Q1>>Q2;
			count=0;
			for (i=Q1; i<=Q2; i++){
				k = Q2-i+1;
				count_temp = 0;
				flag:
					inc=0;
					count_temp++;
					j = count_temp;
					if (count_temp > k){
						continue;
					}
					AND = A[i+inc-1];
					while(j){
						AND = AND&A[i+inc-1];
						j--;
						inc++;
					}
					if (isPerfectSquare(AND))
						count++;
					goto flag;
			}
			cout<<count<<"\n";
		}
		T--;
	}
	return 0;
}

bool isPerfectSquare(long long int x) 
{    
  long double sr = sqrt(x); 
   
  return ((sr - floor(sr)) == 0); 
} 
