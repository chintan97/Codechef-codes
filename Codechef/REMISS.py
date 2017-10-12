#https://www.codechef.com/problems/REMISS
#Chintan Patel 24-12-2016

T = input()
while T>0:
	A,B = [int(x) for x in raw_input().split()]
	print max(A,B),A+B
	T -= 1