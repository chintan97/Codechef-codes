#https://www.codechef.com/problems/RESQ
#Chintan Patel 30-12-2016

import math
T = input()
while T>0:
	N = input()
	ans = N
	for i in range(1,int(math.floor(math.sqrt(N)))+1):
		if N%i == 0:
			temp = abs((N/i)-i)
			if ans > temp:
				ans = temp
				
	print ans
	T -= 1