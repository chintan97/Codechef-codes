#https://www.codechef.com/problems/NUMGAME2
#Chintan Patel 28-12-2016

T = input()
while T>0:
	if input()%4 == 1: print 'ALICE'
	else: print 'BOB'
	T -= 1