#https://www.codechef.com/problems/FRGTNLNG
#Chintan Patel 2-1-2017

T = input()
Str = list()
A = list()
while T>0:
	N,K = [int(x) for x in raw_input().split()] 
	W = [str(s) for s in raw_input().split()]
	del Str
	Str = list()
	while K:
		A = [str(x) for x in raw_input().split()]
		for i in range(1,len(A)):
			Str.append(A[i])
		K -= 1
	
	for i in W:
		if Str.count(i)>0:
			print 'YES',
		else:
			print 'NO',
			
	print '\n'
	T -= 1