#https://www.codechef.com/problems/FLOW017
#Chintan Patel 24-12-2016

T = input()
A = list()
while T>0:
	A = [int(x) for x in raw_input().split()]
	temp = max(A)
	A.remove(temp)
	print max(A)
	T -= 1