#https://www.codechef.com/problems/MNMX
#Chintan Patel 23-12-2016

T = input()
A = list()
while T>0:
	N = input()
	A = [int(x) for x in raw_input().split()]
	temp = min(A)
	print temp*(N-1)
	T -= 1