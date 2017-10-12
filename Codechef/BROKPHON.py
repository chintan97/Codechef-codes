#https://www.codechef.com/problems/BROKPHON
#Chintan Patel 5-1-2016
T = input()
while T:
	cnt = 0
	N = input()
	A = [int(x) for x in raw_input().split()]
	for i in range(N):
		if i != N-1 and A[i] != A[i+1]:
			cnt += 1
		elif A[i] != A[i-1] and i != 0:
			cnt += 1
	print cnt
	T -= 1 