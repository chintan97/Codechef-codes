#https://www.codechef.com/problems/FLOW002
#Chintan Patel 24-12-2016

T = input()
while T>0:
	A,B = [int(x) for x in raw_input().split()]
	print A%B
	T -= 1