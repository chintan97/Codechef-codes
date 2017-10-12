#https://www.codechef.com/problems/PUPPYGM
#Chintan Patel 5-1-2016 
 
T = input()
while T:
	A,B = [int(x) for x in raw_input().split()]
	if A%2 == 0 and B%2 == 0:
		print 'Tuzik'
	elif A%2 != 0 and B%2 != 0:
		print 'Vanka'
	else:
		print 'Tuzik'
	T -= 1 