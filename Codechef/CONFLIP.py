#https://www.codechef.com/problems/CONFLIP
#Chintan Patel 27-12-2016

T = input()
while T>0:
	G = input()
	while G>0:
		N,I,Q = [int(x) for x in raw_input().split()]
		if N == 1:
			if Q == 1:
				print I/2
			else:
				print I - I/2
				
		else:
			if Q == 2:
				print I/2
			else:	
				print I - I/2
		G -= 1
	T -= 1