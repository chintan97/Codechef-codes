#https://www.codechef.com/problems/TWOSTR
#Chintan Patel 23-12-2016

T = input()
while T>0:
	X = raw_input()
	Y = raw_input()
	a = 'Yes'
	
	for i in range(0,len(X)):
		if X[i] == '?' or Y[i] == '?':
			continue
		if X[i] != Y[i]:
			a = 'No'
			break
			
	print a
	T -= 1