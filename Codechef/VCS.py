#https://www.codechef.com/problems/VCS
#Chintan Patel 22-12-2016

T = input()
A = list()
B = list()
while T>0:
	N,M,K = [int(x) for x in raw_input().split()]
	A = [int(x) for x in raw_input().split()]
	B = [int(x) for x in raw_input().split()]
	check = list()
	for i in range(N+1):
		check.append(0)
		
	for i in A:
		check[i] += 1
		
	for i in B:
		check[i] += 1 
		
	ti = 0
	uu = 0
	for i in range(1,N+1):
		if check[i] == 0:
			uu += 1
		elif check[i] == 2:
			ti += 1
			
	print ti,uu
	T -= 1