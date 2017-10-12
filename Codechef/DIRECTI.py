#https://www.codechef.com/problems/DIRECTI
#Chintan Patel 3-1-2016

T = input()
A = []
while T:
	N = input()
	del A[:]
	for i in range(N):
		A.append(raw_input())
	
	cnt = 1
	A.reverse()
	for X in A:
		if X.find('Left') != -1:
			temp = X[5:]
			if cnt == 1:
				print 'Begin',temp
				cnt = 10
			else:
				print next,temp
			next = 'Right'
		elif X.find('Right') != -1:
			temp = X[6:]
			if cnt == 1:
				print 'Begin',temp
				cnt = 10
			else:
				print next,temp
			next = 'Left'
		else:
			temp = X[6:]
			print next,temp
	T -= 1