#https://www.codechef.com/problems/PRB01
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N = input()
	flag = 1
	for i in range(2,N/2):
		if N%i == 0:
			flag = 0
			break
			
	if flag == 1: print 'yes'
	else: print 'no'
	T -= 1