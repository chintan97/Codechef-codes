#https://www.codechef.com/problems/CHOPRT
#Chintan Patel 23-12-2016

T = input()
while T>0:
	A,B = [int(x) for x in raw_input().split()]
	if A < B: print '<'
	elif A > B: print '>'
	else: print '='
	T -= 1