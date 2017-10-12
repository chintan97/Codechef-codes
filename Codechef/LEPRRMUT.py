#https://www.codechef.com/problems/LEPERMUT
#Chintan Patel 28-12-2016

T = input()
A = []
while T>0:
	N = input()
	A = [int(x) for x in raw_input().split()]
	ap = 0
	lp = 0
	for i in range(0,N):
		for j in range(i,N):
			if A[i] > A[j]:
				ap += 1
				
	for i in range(0,N-1):
		if A[i] > A[i+1]:
			lp += 1
			
	if ap == lp: print 'YES'
	else: print 'NO'
	T -= 1