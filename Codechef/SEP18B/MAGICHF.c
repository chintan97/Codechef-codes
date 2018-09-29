//https://www.codechef.com/SEPT18B/problems/MAGICHF
//Chintan Patel 9-9-2018

#include<stdio.h>

int main(){
	int N, S, T, A, B, X;
	scanf("%d", &T);
	while (T > 0){
		scanf("%d%d%d", &N, &X, &S);
		while (S > 0){
			scanf("%d%d", &A, &B);
			if (A == X){
				X = B;
			}
			else if (B == X){
				X = A;
			}
			S--;
		}
		printf("%d", X);
		T--;
	}
	return 0;
}
