#https://www.codechef.com/problems/FCTRL
#Chintan Patel 24-12-2016

T = input()
while T>0:
	N = input()
	cnt = 0
	temp = 5
	while N/temp > 0:
		cnt += abs(N/temp)
		temp *= 5
		
	print cnt
	T -= 1