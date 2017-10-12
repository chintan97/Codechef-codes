#https://www.codechef.com/problems/FLOW013
#Chintan Patel 24-12-2016

T = input()
while T>0:
	A,B,C = [int(x) for x in raw_input().split()]
	if A == 0 or B == 0 or C == 0: print 'NO'
	elif A+B+C == 180: print 'YES'
	else: print 'NO'
	T -= 1