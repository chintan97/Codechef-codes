#https://www.codechef.com/problems/COMM3
#Chintan Patel 24-12-2016

import math
T = input()
A = list()
B = list()
C = list()
while T>0:
	N = input()
	A = [int(x) for x in raw_input().split()]
	B = [int(x) for x in raw_input().split()]
	C = [int(x) for x in raw_input().split()]
	dab = math.sqrt(abs((B[1]-A[1])*(B[1]-A[1]) + (B[0]-A[0])*(B[0]-A[0])))
	dac = math.sqrt(abs((C[1]-A[1])*(C[1]-A[1]) + (C[0]-A[0])*(C[0]-A[0])))
	dbc = math.sqrt(abs((C[1]-B[1])*(C[1]-B[1]) + (C[0]-B[0])*(C[0]-B[0])))
	if (dab <= N or dac <= N) and (dac <= N or dbc <= N) and (dbc <= N or dab <= N): print 'yes'
	else: print 'no'
	T -= 1