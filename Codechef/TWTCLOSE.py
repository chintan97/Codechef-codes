#https://www.codechef.com/problems/TWTCLOSE
#Chintan Patel 24-03-2017

N, K = [int(x) for x in raw_input().split()]
twt = [0]*N
while K:
	A = raw_input()
	if A == 'CLOSEALL':
		twt = [0]*N
	else:
		X, Y = A.split()
		twt[int(Y)-1] = 0 if twt[int(Y)-1]==1 else 1
	print twt.count(1)
	K -= 1