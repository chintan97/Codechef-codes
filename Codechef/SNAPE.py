#https://www.codechef.com/problems/SNAPE
#Chintan Patel 24-12-2016

import math
T = input()
while T>0:
	B,LS = [int(x) for x in raw_input().split()]
	print math.sqrt(LS*LS - B*B),math.sqrt(LS*LS + B*B)
	T -= 1