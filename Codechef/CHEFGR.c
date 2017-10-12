//https://www.codechef.com/problems/CHEFGR
//Chintan Patel 4-1-2016

#include <stdio.h>

int main(void) {
	// your code goes here
	int T,max,flag,N,M,i,A[101],temp,sum;
	scanf("%d",&T);
	while(T)
	{
	    max = 0;
	    sum = 0;
	    scanf("%d %d",&N,&M);
	    for(i=0;i<N;i++)
	    {
	        scanf("%d",&A[i]);
	        if(max < A[i])
	            max = A[i];
	        sum += A[i];
	    }
	    temp = max*N;
	    flag = temp-sum;
	    if(M >= flag)
	    {
	        M -= flag;
	        if(M%N == 0)
	            printf("\nYes");
	        else
	            printf("\nNo");
	    }
	    else
	        printf("\nNo");
	    T--;
	};
	return 0;
}

