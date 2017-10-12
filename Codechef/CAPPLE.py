#https://www.codechef.com/problems/CAPPLE
#Chintan Patel 5-1-2017

T = input()
while T:
	N = input()
	A = [int(x) for x in raw_input().split()]
	print len(set(A))
	T -= 1