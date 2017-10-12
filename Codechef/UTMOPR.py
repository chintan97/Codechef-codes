#https://www.codechef.com/problems/UTMOPR
#Chintan Patel 20-12-2016

T = input()
S = list()
while T>0:
	sum = 0
	N,K = [int(x) for x in raw_input().split()]
	S = [int(x) for x in raw_input().split()]
	if K>1:
		print "even"
	else:
		for i in S:
			sum += i
		if sum%2 == 0:
			print "odd"
		else:
			print "even"
		
	T -= 1