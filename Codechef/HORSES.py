#https://www.codechef.com/problems/HORSES
#Chintan Patel 27-12-2016

T = input()
S = list()
while T>0:
	N = input()
	S = [int(x) for x in raw_input().split()]
	S.sort()
	min = S[1]-S[0]
	for i in range(1,N):
		if min > S[i]-S[i-1]:
			min = S[i]-S[i-1]
			
	print min
	T -= 1