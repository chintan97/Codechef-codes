#https://www.codechef.com/FEB17/problems/CHEFAPAR
#Chintan Patel 9-2-2017

T = input()
while T:
	B = []
	N = input()
	A = [int(x) for x in raw_input().split()]
	for i in range(len(A)):
		if A[i] == 0:
			B = A[i:]
			break
	print int(len(B)*1100-B.count(1)*1000)
	T -= 1