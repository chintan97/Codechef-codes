#https://www.codechef.com/problems/FLOW009
#Chintan Patel 23-12-2016

T = input()
while T>0:
	q,p = [int(x) for x in raw_input().split()]
	if q < 1000: print "%.6f"%(p*q)
	else: print "%.6f"%(p*q*0.9)
	T -= 1