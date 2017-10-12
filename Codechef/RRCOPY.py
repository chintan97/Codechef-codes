#https://www.codechef.com/problems/RRCOPY
#Chintan Patel 30-12-2016

from collections import OrderedDict
T = input()
while T>0:
	N = input()
	A = [str(x) for x in raw_input().split()]
	B = ",".join(OrderedDict.fromkeys(A))
	print B.count(',')+1
	T -= 1