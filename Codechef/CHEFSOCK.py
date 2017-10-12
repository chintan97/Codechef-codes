#https://www.codechef.com/problems/CHEFSOCK
#Chintan Patel 9-1-2016

JC,SC,M = [int(x) for x in raw_input().split()]
M -= JC
x = M/SC
if x%2 == 0:
	print 'Lucky Chef'
else:
	print 'Unlucky Chef'