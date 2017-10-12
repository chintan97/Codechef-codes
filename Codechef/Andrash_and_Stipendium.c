//Chintan Patel
//Jul-2016,Codeshef

#include<stdio.h>
void check(int x[]);
int main()
{
	int n,i=1,x[10010],j,temp;
	//int sub[10010];
	int mrk[100][100];
	scanf("%d",&n);
	temp=n;
	while(n!=0)
	{
		scanf("%d",&x[i]);
		for(j=1;j<=x[i];j++)
		{
			scanf("%d",&mrk[i][j]);
			//void check(mrk[i]);
		}
		i++;
		n--;
	}
	i--;
	//printf("\n%d",i);
	n=temp;
	temp=i;
	i=1;
	while(n!=0)
	{
		check(mrk[i]);
		i++;
		n--;
	}
}
void check(int mk[])
{
	int i=1,flag=0;
	float avg=0;
	while(mk[i]!='\0')
	{
		if(mk[i]<2)
		{
			printf("\nNo");
			break;
		}
		else if(mk[i]>5)
		{
			printf("\nInvalid");
		}
		else if(mk[i]==5)
		{
			avg+=mk[i];
			flag++;
		}
		else 
			avg+=mk[i];
		i++;
	}
	i--;
	avg=avg/i;
	//printf("\n%f %d",avg,i);
	if(flag!=0 && avg>=4)
		printf("\nYes");
	else
		printf("\nNo");
}
