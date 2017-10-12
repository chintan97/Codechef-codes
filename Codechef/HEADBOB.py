#https://www.codechef.com/problems/HEADBOB
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N = input()
	G = raw_input()
	y = G.count('Y')
	n = G.count('N')
	i = G.count('I')
	if i > 0: print 'INDIAN'
	elif y > 0: print 'NOT INDIAN'
	else: print 'NOT SURE'
	T -= 1