#https://www.codechef.com/problems/OMWG
#Chintan Patel 19-12-2016

T = input()
while T>0:
	N,M = [int(x) for x in raw_input().split()]
	print (N-1)+(M-1)+2*(N-1)*(M-1)
	T -= 1