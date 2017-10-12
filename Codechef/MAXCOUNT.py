#https://www.codechef.com/problems/MAXCOUNT
#Chintan Patel 9-1-2016 
 
T = input()
while T:
	N = input()
	A = [int(x) for x in raw_input().split()]
	B = list(set(A))
	maxc = A.count(B[0])
	temp = B[0]
	for i in B:
		if maxc < A.count(i):
			maxc = A.count(i)
			temp = i
		elif maxc == A.count(i) and temp > i:
		    maxc = A.count(i)
		    temp = i
	print temp,maxc
	T -= 1 