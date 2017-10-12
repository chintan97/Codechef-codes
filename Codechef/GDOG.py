#https://www.codechef.com/problems/GDOG
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N,K = [int(x) for x in raw_input().split()]
	max = 0
	for i in range(1,K+1):
		temp = N%i
		if temp > max:
			max = temp
	
	print max
	T -= 1