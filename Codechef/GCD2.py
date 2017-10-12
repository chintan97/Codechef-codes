#https://www.codechef.com/problems/GCD2
#Chintan Patel 28-12-2016

from fractions import gcd
T = input()
while T>0:
	A,B = [int(x) for x in raw_input().split()]
	print gcd(A,B)
	T -= 1