#https://www.codechef.com/problems/PALL01
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N = input()
	temp = N
	ch = 0
	while N > 0:
		ch = (N%10) + (ch*10)
		N /= 10
	
	if temp == ch: print 'wins'
	else: print 'losses'
	T -= 1