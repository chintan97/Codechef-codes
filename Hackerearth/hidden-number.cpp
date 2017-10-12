#include<iostream>
#include<conio.h>
int main()
{
	int T, N, i, j, k, flag=0, count;
	int A[10000];
	std::cin >> T;
	while (T > 0)
	{
		std::cin >> N;
		for (i=0; i<N; i++)
		{
			std::cin >> A[i];
		}
		for (i=0; i<N; i++)
		{
			flag = 0;
			count = 0;
			cp:
			for (j=i+1; j<N; j++)
			{
				if (A[i] == A[j])
				{
					count++;
					for (k=j; k<N; k++)
					{
						A[k] = A[k+1];
					}
					N--;
					goto cp;
				}
			}
			if (count == 0)
			{
				std::cout << A[i];
				break;
			}
		}
		T--;
	}
	return 0;
}
