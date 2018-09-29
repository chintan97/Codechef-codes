#https://www.codechef.com/JAN17/problems/CATSDOGS
#Chintan Patel 6-1-2016

T = input()
while T:
	C,D,L = [int(x) for x in raw_input().split()]
	if L%4 != 0:
		print 'no'
	elif (C+D)*4 < L:
		print 'no'
	elif (C+D)*4 == L:
		print 'yes'
	elif D*4 > L:
		print 'no'
	else:
		temp = D*2
		x = temp-C
		if x >= 0:
			if D*4 > L:
				print 'no'
			else:
				print 'yes'
		else:
			if (D+abs(x))*4 > L:
				print 'no'
			else:
				print 'yes'
	T -= 1