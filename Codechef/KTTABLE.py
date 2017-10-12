#https://www.codechef.com/problems/KTTABLE
#Chintan Patel 21-12-2016

T = input()
A = list()
B = list()
while T>0:
	N = input()
	A = [int(x) for x in raw_input().split()]
	B = [int(x) for x in raw_input().split()]
	cnt = 0
	
	if A[0] >= B[0]:
		cnt += 1
	for i in range(1,N):
		if B[i] <= A[i]-A[i-1]:
			cnt += 1
			
	print cnt
	T -= 1