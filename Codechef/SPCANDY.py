#https://www.codechef.com/problems/SPCANDY
#Chintan Patel 30-12-2016

T = input()
while T>0:
	N,K = [int(x) for x in raw_input().split()]
	if K > 0: print N/K,N%K
	else: print 0,N
	T -= 1