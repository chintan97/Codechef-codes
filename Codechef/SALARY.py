#https://www.codechef.com/problems/SALARY
#Chintan Patel 31-12-2016

T = input()
while T:
	N = input()
	W = [int(x) for x in raw_input().split()]
	W.sort()
	D = 0
	temp = W[0]
	if N == 1:
		print 0
	else:
		for i in range(1,N):
			D += W[i]-temp
		print D
	T -= 1