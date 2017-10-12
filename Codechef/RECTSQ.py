#https://www.codechef.com/problems/RECTSQ
#Chintan Patel 22-12-2016
from fractions import gcd

T = input()
while T>0:
	M,N = [int(x) for x in raw_input().split()]
	print (M/gcd(M,N))*(N/gcd(M,N))
	T -= 1