#https://www.codechef.com/problems/ANUBTG
#Chintan Patel 2-1-2016

T = input()
while T:
	N = input()
	A = [int(x) for x in raw_input().split()]
	A.sort(reverse=True)
	
	sum = 0
	for i in range(0,N,4):
		sum += A[i]
	for i in range(1,N,4):
		sum += A[i]
	print sum
	T -= 1