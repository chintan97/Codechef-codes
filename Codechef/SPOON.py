#https://www.codechef.com/problems/SPOON
#Chintan Patel 4-1-2016

T = input()
A = []
while T:
	flag = 0
	del A[:]
	R,C = [int(x) for x in raw_input().split()]
	temp = 0
	for i in range(R):
		A.append(raw_input().lower())
		if A[i].find('spoon') != -1:
			flag = 1
	if flag == 0:
		for i in range(R-4):
			for j in range(C):
				if A[i][j]=='s' and A[i+1][j]=='p' and A[i+2][j]=='o' and A[i+3][j]=='o' and A[i+4][j]=='n':
					flag = 1
					break
		if flag == 0:
			print 'There is indeed no spoon!'
	if flag == 1:
		print 'There is a spoon!'
	T -= 1