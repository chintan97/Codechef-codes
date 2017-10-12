#https://www.codechef.com/problems/TREEROOT
#Chintan Patel 30-3-2017

T = input()
while T:
	N = input()
	sumA, sumB = 0, 0
	while N:
		A, B = [int(x) for x in raw_input().split()]
		sumA += A
		sumB += B
		N -= 1
	print sumA - sumB
	T -= 1