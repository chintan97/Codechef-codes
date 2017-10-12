#https://www.codechef.com/problems/JOHNY
#Chintan Patel 27-12-2016

T = input()
A = list()
while T>0:
	N = input()
	A = [int(x) for x in raw_input().split()]
	K = input()
	val = A[K-1]
	A.sort()
	for i in range(0,N):
		if A[i] == val:
			print i+1
			break
	T -= 1