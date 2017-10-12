#https://www.codechef.com/problems/CHEFSTON
#Chintan Patel 3-1-2016

T = input()
while T:
	N,K = [int(x) for x in raw_input().split()]
	max = 0
	A = [int(x) for x in raw_input().split()]
	B = [int(x) for x in raw_input().split()]
	for i in range(N):
		temp = K/A[i]
		if max < temp*B[i]:
			max = temp*B[i]
	print max
	T -= 1 