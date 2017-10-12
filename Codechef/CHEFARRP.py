#https://www.codechef.com/problems/CHEFARRP
#Chintan Patel 21-12-2016

T = input()
while T>0:
	n = input()
	A = [int(x) for x in raw_input().split()]
	cnt = 0
	for i in range(0,n):
		sum,pro = 0,1
		for j in range(i,n):
			sum += A[j]
			pro *= A[j]
			if sum == pro:
				cnt += 1
	
	print cnt
	T -= 1