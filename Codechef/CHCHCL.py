#https://www.codechef.com/problems/CHCHCL
#Chintan Patel 20-12-2016

T = input()
while T>0:
	n,m = [int(x) for x in raw_input().split()]
	if n*m%2 == 0:
		print "Yes"
	else:
		print "No"
	T -= 1