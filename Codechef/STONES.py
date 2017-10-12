#https://www.codechef.com/problems/STONES
#Chintan Patel 27-12-2016

from collections import OrderedDict
T = input()
while T>0:
	J = raw_input()
	S = raw_input()
	cnt = 0
	J_new = "".join(OrderedDict.fromkeys(J))
	for i in J_new:
		cnt += S.count(i)
		
	print cnt
	T -= 1