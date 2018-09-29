#include<iostream>
using namespace std;

int main(){
	long long int n, i, j, count=0, sum, min_so_far;
	long long int A[200000];
	long long int t;
	cin>>n>>t;
	for (i=0; i<n; i++){
		cin>>A[i];
	}
	i=0;
	min_so_far = A[0];
	while (i < n){
		sum = A[i];
		j = i;
		if (sum < t)
			count++;
		else{
			min_so_far = A[i];
			j = n-1;	
		}
		while (j < n-1){
			j++;
			sum += A[j];
			if (sum < t)
				count++;
			else{
				sum -= A[j];
				if (sum+min_so_far < t){
					count++;
					min_so_far = sum+min_so_far;
					j = n-1;
				}
				else{
					min_so_far = sum;
					j = n-1;	
				}	
			}
		}
		i++;
	}
	cout<<count;
	return 0;
}
