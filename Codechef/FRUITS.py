#https://www.codechef.com/problems/FRUITS
#Chintan Patel 22-12-2016

T = input()
while T>0:
	N,M,K = [int(x) for x in raw_input().split()]
	
	temp = max(N,M)-min(N,M)
	x = temp - K
	if x < 0:
		x = 0
	print x
	T -= 1