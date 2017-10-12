#https://www.codechef.com/problems/TSORT
#Chintan Patel 3-1-2016

N = input()
A = []
for i in range(N):
	A.append(input())
A.sort()
for i in A:
	print i