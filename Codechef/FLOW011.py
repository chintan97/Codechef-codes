#https://www.codechef.com/problems/FLOW011
#Chintan Patel 23-12-2016

T = input()
while T>0:
	s = input()
	if s < 1500:
		print 2*s
	else:
		print "%g"%(s*1.98 + 500)
	T -= 1