#https://www.codechef.com/problems/LEBOMBS
#Chintan Patel 30-12-2016

T = input()
while T>0:
	N = input()
	S = raw_input()
	a = [0]*N
	if N == 1:
		if S[0] == '1': print 0
		else: print 1
	else:
		for i in range(N):
			if i == 0 and S[0] == '1':
				a[0], a[1] = 1,1
			elif i == N-1 and S[N-1] == '1':
				a[N-2], a[N-1] = 1,1
			elif S[i] == '1':
				a[i-1], a[i], a[i+1] = 1,1,1
			
		print a.count(0)
	T -= 1