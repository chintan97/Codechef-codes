//Chintan Patel
//Jul-2016,Codeshef
//https://www.codechef.com/problems/HS08TEST

#include<stdio.h>
int main()
{
	float amount=0;
	int withdr=0;
	scanf("%d %f",&withdr,&amount);
	if(amount>=0 && amount<=2000 && withdr>0 && withdr<=2000)
	{
		if(withdr%5==0)
		{
			if(withdr+0.5<amount)
			{
				amount=amount-(withdr+0.50);
				printf("\n%.2f",amount);
			}
			else
			{
				printf("\n%.2f",amount);
			}
		}
		else
		{
			printf("\n%.2f",amount);
		}
	}
	return 0;
}
