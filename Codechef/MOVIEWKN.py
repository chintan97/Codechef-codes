#https://www.codechef.com/problems/MOVIEWKN
#Chintan Patel 21-12-2016

T = input()
L = list()
R = list()
while T>0:
	n = input()
	L = [int(x) for x in raw_input().split()]
	R = [int(x) for x in raw_input().split()]
	flag = 0
	max = L[0]*R[0]
	for i in range(1,n):
		temp = L[i]*R[i]
		if temp > max:
			flag = i
			max = temp
		elif temp == max:
			if R[i] > R[flag]:
				flag = i
				
	print flag+1
	T -= 1