//https://www.codechef.com/SEPT18B/problems/CHEFADV
//Chintan Patel 9-9-2018

#include<stdio.h>

int main(){
	long long int T, N, M, X, Y, F = 0;
	scanf("%lld", &T);
	while (T > 0){
		scanf("%lld%lld%lld%lld", &N, &M, &X, &Y);
		N--;
		M--;
		if (N == 0){
			if (M%Y == 0)
				F = 1;
			else
				F = 0;
		}
		else if (M == 0){
			if (N%X == 0)
				F = 1;
			else
				F = 0;
		}
		else if ((X == 1 && M%Y < 2) || (Y == 1 && N%X < 2))
			F = 1;
		else if ((N%X == M%Y) && (N%X == 1 || N%X == 0))
			F = 1;
		else
			F = 0;
		if (F == 1)
			printf("Chefirnemo\n");
		else
			printf("Pofik\n");
		T--;
	}
	return 0;
}
