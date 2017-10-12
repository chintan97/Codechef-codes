#https://www.codechef.com/problems/FLOW004
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N = input()
	sum = N%10
	rev = 0
	while N > 0:
		rev = (N%10) + (rev*10)
		N /= 10
	
	print sum + (rev%10)
	T -= 1